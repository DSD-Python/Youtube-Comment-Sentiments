from api import replies, channel_snippet
import re, io
from datetime import datetime
from dateutil import parser
from symspellpy import SymSpell, Verbosity
import numpy as np
import matplotlib.pyplot as plt
'''
Statistical Analysis and Graphs
'''

file = open('NRC-Emotion-Lexicon-Wordlevel-v0.92.txt', 'r').read()
pattern = r'(\w*)\s*(\w*)\s*(\d)'
sentiments = {}

for word in re.findall(pattern, file):
    if int(word[2]) == 1:
        if word[0] in sentiments.keys():
            sentiments[word[0]].append(word[1])
        else: 
            sentiments[word[0]] = [word[1]]

sym_spell = SymSpell()
sym_spell.load_dictionary("frequency_dictionary_en_82_765.txt", 0, 1)


# recieves comment list and turn into arrays 
def from_comment(youtube, comment):
    comments = []
    cmt_ages = []
    users = []
    user_ages = []

    # for each top level comment 
    for cmt_thread in comment:
        # if it has replies 
        if 'replies' in cmt_thread.keys() and len(cmt_thread['replies']['comments']) > 0:
            # get the top 100 replies 
            reps = replies(youtube, cmt_thread['id'])
            # add each reply to the list
            for rep in reps['items']:
                comments.append(rep['textDisplay'])
                cmt_ages.append(parser.isoparse(rep['publishedAt']))
                # if the user is not in the user list add them and their age
                if rep['snippet']['authorChannelId']['value'] not in users:
                    users.append(rep['snippet']['authorChannelId']['value'])
                    user_ages.append(parser.isoparse(channel_age(youtube, rep['snippet']['authorChannelId']['value'])))
        # add top level comment
        comments.append(cmt_thread['snippet']['topLevelComment']['snippet']['textDisplay'])
        cmt_ages.append(parser.isoparse(cmt_thread['snippet']['topLevelComment']['snippet']['publishedAt']))
        # if the user is not in the user list add them and their age
        if cmt_thread['snippet']['channelId'] not in users:
            users.append(cmt_thread['snippet']['channelId'])
            user_ages.append(parser.isoparse(channel_age(youtube, cmt_thread['snippet']['channelId'])))

    comments = np.array(comments)
    cmt_ages = np.array([(datetime.now(age.tzinfo) - age).days*24 + (datetime.now(age.tzinfo) - age).seconds//3600 for age in cmt_ages])
    users = np.array(users)
    user_ages = np.array([(datetime.now(age.tzinfo) - age).days*24 + (datetime.now(age.tzinfo) - age).seconds//3600 for age in user_ages])

    return (comments, cmt_ages, users, user_ages)

def channel_age(youtube, channel_id): 
    return channel_snippet(youtube, channel_id)['publishedAt']

def sentiment_stats(comments):
    exp = r"\w{3,}"
    comments_cleaned = []
    for i in range(comments.size):
        spell_checked = []
        for word in re.findall(exp, comments[i]):
            check = sym_spell.lookup(word, Verbosity.CLOSEST)
            if len(check) > 0:
                spell_checked.append(check[0].term)
            else:
                spell_checked.append(word)
        comments_cleaned.append(spell_checked)

    props = {
        "anger" : [],
        "anticipation" : [], 
        "disgust" : [], 
        "fear" : [], 
        "joy" : [], 
        "sadness" : [], 
        "surprise" : [], 
        "trust" : [], 
        "negative" : [], 
        "positive" : [], 
    }

    for comment in comments_cleaned:
        total = 0
        counts = {
        "anger" : 0,
        "anticipation" : 0, 
        "disgust" : 0, 
        "fear" : 0, 
        "joy" : 0, 
        "sadness" : 0, 
        "surprise" : 0, 
        "trust" : 0, 
        "negative" : 0, 
        "positive" : 0, 
        }
        # if comment contains no meaningful information add all zeros
        if len(comment) == 0:
            for key, value in counts.items():
                props[key].append(value)
            continue
        # else count sentiments 
        for word in comment:
            if word in sentiments.keys():
                for sentiment in sentiments[word]:
                    counts[sentiment] += 1
                total+=1
        # add prop of counted words each sentiment represented
        for key, value in counts.items():
            props[key].append(value / total if total > 0 else value)

    img_buffers = []
    # histograms
    for key, value in props.items():
        if key not in ['positive', 'negative']:
            plt.hist(props[key], bins=30, color='skyblue', edgecolor='black')
            plt.xlabel(f"% of Comment - {key}")
            plt.ylabel('Comments Frequency')
            plt.title(f"{key[0].upper()}{key[1:]} of Comments")

            buffer = io.BytesIO()
            img_buffers.append(buffer)
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            plt.clf()


    pos_v_neg = []
    for i in range(len(props['positive'])):
        pos_v_neg.append(props['positive'][i]- props['negative'][i])

    plt.hist(pos_v_neg, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel(f"% of Comment Positivity - Negativity")
    plt.ylabel('Comments Frequency')
    plt.title(f"Overall Sentiment of Comments")

    buffer = io.BytesIO()
    img_buffers.append(buffer)
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.clf()

    means = []
    labels = []
    sentiment_df = []
    for key, value in props.items():
        means.append(np.mean(np.array(props[key])))
        labels.append(key)
        value.insert(0, key)
        sentiment_df.append(value)

    fig, ax = plt.subplots()
    ax.bar(labels, means, color='skyblue')
    ax.set_title("Mean Comment Sentiments")
    ax.set_ylabel("Mean \% of comment")
    ax.set_xlabel("Sentiment/Emotion")
    plt.xticks(rotation=45, ha="right")

    buffer = io.BytesIO()
    img_buffers.append(buffer)
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.clf()

    return np.array(sentiment_df), img_buffers 
    
def age_stats(cmt_ages, user_ages):
    img_buffers = []
    plt.hist(cmt_ages, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel(f"Comment Age")
    plt.ylabel('Frequency')
    plt.title(f"Ages of Comments (hours old)")

    buffer = io.BytesIO()
    img_buffers.append(buffer)
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.clf()

    plt.hist(user_ages, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel(f"User Age")
    plt.ylabel('Frequency')
    plt.title(f"Ages of Users (hours old)")

    buffer = io.BytesIO()
    img_buffers.append(buffer)
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.clf()

    return cmt_ages, user_ages, img_buffers

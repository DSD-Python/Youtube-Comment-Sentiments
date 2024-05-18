''' 
User Auth & API Requests
'''

import re
from googleapiclient.discovery import build
from env import client_secret


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

def yt_auth():
    flow = InstalledAppFlow.from_client_config(
        client_secret,
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    )

    credentials = flow.run_local_server(host='localhost',
        port=8080, 
        authorization_prompt_message='Please visit this URL: {url}', 
        success_message='The auth flow is complete; you may close this window.',
        open_browser=True)


    return build('youtube', 'v3', credentials=credentials)


#sort = ["date", "rating", "relevance", "title", "viewCount"]
#duration long:(20m, infty) medium:[2m, 20m] short:(0m, 2m)
#safeSearch long: none, moderate, strict
# returns api request with given paramaters
def vid_list(youtube, search_term:str, sort:str="relevance", duration:str="any", safe_search:str="moderate", start=None, end=None):
    regex = r'\w+'
    search_term = ' '.join(re.findall(regex, search_term))

    request = youtube.search().list(
            part="snippet",
            order=sort,
            q=search_term, 
            videoDuration=duration,
            safeSearch=safe_search,
            type="video",
            maxResults=50,
            publishedAfter=start,
            publishedBefore=end,
    )
    response = request.execute()
    if response: 
        return response

    raise HttpError(response)

def comments(youtube, vid_id):
    request = youtube.commentThreads().list(
            part="snippet",
            videoId=vid_id,
            textFormat="plainText",
            maxResults=100
    )
    response = request.execute()
    if response: 
        return response

    raise HttpError(response)

def replies(youtube, cmt_id):
    request = youtube.comments().list(
        part="snippet",
        parentId=cmt_id,
        textFormat="plainText",
        maxResults=100,
    )   
    response = request.execute()
    if response: 
        return response

    raise HttpError(response)

def channel_snippet(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet",
        id=channel_id,
        maxResults=1
    )
    response = request.execute()
    if response: 
        return response['items'][0]['snippet']

    raise HttpError(response)
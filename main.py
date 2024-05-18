import json
import sys 
import numpy as np
from urllib import request
from datetime import datetime
from dateutil import parser
from api import yt_auth, vid_list, comments
from do_stat import from_comment, sentiment_stats, age_stats
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesigngylUYJ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QMouseEvent, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSplitter, QStatusBar, QVBoxLayout,
    QWidget, QToolBar, QFileDialog)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Main Window")
        MainWindow.resize(922, 762)
        

        self.youtube = None
        self.vid_options = []

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.filters = QScrollArea(self.splitter)
        self.filters.setObjectName(u"filters")
        self.filters.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.filters.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 310, 721))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.user = QPushButton(self.scrollAreaWidgetContents)
        self.user.setObjectName(u"user")

        self.verticalLayout_6.addWidget(self.user)

        self.search_filters = QSplitter(self.scrollAreaWidgetContents)
        self.search_filters.setObjectName(u"search_filters")
        self.search_filters.setOrientation(Qt.Orientation.Vertical)
        self.search_filters.setOpaqueResize(True)
        self.sort = QGroupBox(self.search_filters)
        self.sort.setObjectName(u"sort")
        self.sort.setEnabled(True)
        self.sort.setFlat(False)
        self.sort.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.sort)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title = QRadioButton(self.sort)
        self.title.setObjectName(u"title")

        self.gridLayout_2.addWidget(self.title, 1, 0, 1, 1)

        self.relevance = QRadioButton(self.sort)
        self.relevance.setObjectName(u"relevance")
        self.relevance.setChecked(True)

        self.gridLayout_2.addWidget(self.relevance, 0, 0, 1, 1)

        self.views = QRadioButton(self.sort)
        self.views.setObjectName(u"views")

        self.gridLayout_2.addWidget(self.views, 2, 0, 1, 1)

        self.date = QRadioButton(self.sort)
        self.date.setObjectName(u"date")

        self.gridLayout_2.addWidget(self.date, 3, 0, 1, 1)

        self.search_filters.addWidget(self.sort)
        self.search_range = QGroupBox(self.search_filters)
        self.search_range.setObjectName(u"search_range")
        self.gridLayout_3 = QGridLayout(self.search_range)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox = QCheckBox(self.search_range)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.range_cont = QGroupBox(self.search_range)
        self.range_cont.setObjectName(u"range_cont")
        self.verticalLayout = QVBoxLayout(self.range_cont)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.range_cont)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.searchStart = QDateTimeEdit(self.range_cont)
        self.searchStart.setObjectName(u"searchStart")

        self.verticalLayout.addWidget(self.searchStart)

        self.label_2 = QLabel(self.range_cont)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.searchEnd = QDateTimeEdit(self.range_cont)
        self.searchEnd.setObjectName(u"searchEnd")

        self.verticalLayout.addWidget(self.searchEnd)


        self.gridLayout_3.addWidget(self.range_cont, 4, 0, 3, 1)

        self.search_filters.addWidget(self.search_range)
        self.duration = QGroupBox(self.search_filters)
        self.duration.setObjectName(u"duration")
        self.gridLayout = QGridLayout(self.duration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.long_2 = QRadioButton(self.duration)
        self.long_2.setObjectName(u"long_2")

        self.gridLayout.addWidget(self.long_2, 4, 0, 1, 1)

        self.short_2 = QRadioButton(self.duration)
        self.short_2.setObjectName(u"short_2")

        self.gridLayout.addWidget(self.short_2, 3, 0, 1, 1)

        self.meduim = QRadioButton(self.duration)
        self.meduim.setObjectName(u"meduim")

        self.gridLayout.addWidget(self.meduim, 1, 0, 1, 1)

        self.any = QRadioButton(self.duration)
        self.any.setObjectName(u"any")
        self.any.setChecked(True)

        self.gridLayout.addWidget(self.any, 0, 0, 1, 1)

        self.search_filters.addWidget(self.duration)
        self.safeSearch = QGroupBox(self.search_filters)
        self.safeSearch.setObjectName(u"safeSearch")
        self.gridLayout_4 = QGridLayout(self.safeSearch)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.none = QRadioButton(self.safeSearch)
        self.none.setObjectName(u"none")

        self.gridLayout_4.addWidget(self.none, 0, 0, 1, 1)

        self.strict = QRadioButton(self.safeSearch)
        self.strict.setObjectName(u"strict")

        self.gridLayout_4.addWidget(self.strict, 2, 0, 1, 1)

        self.moderate = QRadioButton(self.safeSearch)
        self.moderate.setObjectName(u"moderate")
        self.moderate.setChecked(True)

        self.gridLayout_4.addWidget(self.moderate, 1, 0, 1, 1)

        self.search_filters.addWidget(self.safeSearch)

        self.verticalLayout_6.addWidget(self.search_filters)

        self.reset_filters = QPushButton(self.scrollAreaWidgetContents)
        self.reset_filters.setObjectName(u"reset_filters")
        self.reset_filters.setMaximumSize(QSize(341, 16777215))

        self.verticalLayout_6.addWidget(self.reset_filters)

        self.filters.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.filters)
        self.search_results = QGroupBox(self.splitter)
        self.search_results.setObjectName(u"search_results")
        self.verticalLayout_2 = QVBoxLayout(self.search_results)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.search_user = QGroupBox(self.search_results)
        self.search_user.setObjectName(u"search_user")
        self.horizontalLayout = QHBoxLayout(self.search_user)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.query = QLineEdit(self.search_user)
        self.query.setObjectName(u"query")
        self.query.setMinimumSize(QSize(155, 0))

        self.horizontalLayout.addWidget(self.query)

        self.go_search = QPushButton(self.search_user)
        self.go_search.setObjectName(u"go_search")

        self.horizontalLayout.addWidget(self.go_search)


        self.verticalLayout_2.addWidget(self.search_user)

        self.results = QScrollArea(self.search_results)
        self.results.setObjectName(u"results")
        self.results.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 548, 651))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.results.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.results)

        self.splitter.addWidget(self.search_results)

        self.verticalLayout_4.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.reset_filters.clicked.connect(self.moderate.click)
        self.reset_filters.clicked.connect(self.any.click)
        self.reset_filters.clicked["bool"].connect(self.checkBox.setChecked)
        self.reset_filters.clicked.connect(self.relevance.click)
        self.checkBox.toggled.connect(self.range_cont.setDisabled)

        self.query.returnPressed.connect(self.fetch_q)
        self.go_search.pressed.connect(self.fetch_q)
        self.user.pressed.connect(self.sign_in)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"Change User", None))
        self.sort.setTitle(QCoreApplication.translate("MainWindow", u"Sort by", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.relevance.setText(QCoreApplication.translate("MainWindow", u"Relevance", None))
        self.views.setText(QCoreApplication.translate("MainWindow", u"Views", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.search_range.setTitle(QCoreApplication.translate("MainWindow", u"Search Range", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Any", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End:", None))
        self.duration.setTitle(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.long_2.setText(QCoreApplication.translate("MainWindow", u"Long ( >20min)", None))
        self.short_2.setText(QCoreApplication.translate("MainWindow", u" Short (<2 min)", None))
        self.meduim.setText(QCoreApplication.translate("MainWindow", u"Medium (<20 min)", None))
        self.any.setText(QCoreApplication.translate("MainWindow", u"Any", None))
        self.safeSearch.setTitle(QCoreApplication.translate("MainWindow", u"SafeSearch", None))
        self.none.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.strict.setText(QCoreApplication.translate("MainWindow", u"Strict", None))
        self.moderate.setText(QCoreApplication.translate("MainWindow", u"Moderate", None))
        self.reset_filters.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.search_results.setTitle("")
        self.search_user.setTitle("")
        self.query.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.go_search.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
    # retranslateUi

    @Slot()
    def sign_in(self):
        self.youtube = yt_auth()

    @Slot()
    def fetch_q(self):
        for option in self.vid_options:
            option.setParent(None)
        self.centralwidget.setWindowTitle("Dowloading Results... ")
        self.centralwidget.setDisabled(True)
        # collect user options from form 
        text = self.query.text()
        if not len(text) > 0:
            return None
        sort = "relevance"
        for option in [self.relevance, self.title, self.views, self.date]:
            if option.isChecked():
                sort = option.objectName()
        safeSearch = "moderate"
        for option in [self.none, self.moderate, self.strict]:
            if option.isChecked():
                safeSearch = option.objectName()
        duration = "any"
        for option in [self.any, self.meduim, self.short_2, self.long_2]:
            if option.isChecked():
                duration = option.objectName()
        time = []
        if not self.checkBox.isChecked():
            start = self.searchStart.dateTime().toPython()
            end = self.searchEnd.dateTime().toPython()
            time.append(f"({start.year:04f}-{start.month:02f}-{start.day:02f}T{start.hour:02f}:{start.minute:02f}:{start.second:02f}Z)")
            time.append(f"({end.year:04f}-{end.month:02f}-{end.day:02f}T{end.hour:02f}:{end.minute:02f}:{end.second:02f}Z)")
        
        # do Query
        try:
            if self.youtube and len(time) > 0:
                q = vid_list(self.youtube, search_term=text, sort=sort, duration=duration, safe_search=safeSearch, start=time[0], end=time[0])
            else:
                q = vid_list(self.youtube, search_term=text, sort=sort, duration=duration, safe_search=safeSearch)
        except Exception:
            # TODO: add message for http errors
            return None

        for item in q['items']:
            self.vid_options.append(search_result(self, item)) 
        self.centralwidget .setWindowTitle("Search Results")
        self.centralwidget.setDisabled(False)

class search_result(QGroupBox):
    def __init__(self, parent, item) -> None:
        super(search_result, self).__init__()
        self.container = parent
        self.output = None

        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
        months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'] 
        # 1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th 11th 12th 13th 15th 15th 16th 17th 18th 19th 20th 21st 
        suffix = lambda x : 'st' if x in [1, 21, 31] else 'nd' if x in [2, 22] else 'rd' if x in [3, 23] else 'th'
        elap = lambda x : datetime.now(x.tzinfo) - x
        elap_str = lambda x : (f"{x.days/365.25:0.0f} years ago" if x.days // 366 > 0 else
                               f"{x.days/30.5:0.0f} months ago" if x.days // 31 > 0 else
                               f"{x.days:0.0f} days ago" if x.days > 0 else
                               f"{x.seconds // 3600:0.0f} hours ago" if x.seconds // 3600 > 0 else
                               f"{x.seconds // 60:0.0f} minutes ago" if x.seconds // 60 > 0
                               else "seconds ago")

        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        thumbnail = item['snippet']['thumbnails']['default']['url']
        description = item['snippet']['description']
        publish = parser.parse(item['snippet']['publishedAt'])
        publish = f'Published: {days[publish.weekday()]}, {months[publish.month-1]} {publish.day}{suffix(publish.day)}, {publish.year} at {publish.hour+1:02.00f}:{publish.minute:02.00f} ~{elap_str(elap(publish))}'

        self.id = item['id']['videoId']

        self.container.verticalLayout_7.addWidget(self, 0, Qt.AlignmentFlag.AlignTop)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTitle(QCoreApplication.translate("MainWindow", title, None))

        self.setObjectName(u"video_result")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")

        self.img_label = QLabel(self)
        self.img_label.setObjectName(u"result_img_")
        img = request.urlopen(thumbnail).read()
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        self.img_label.setPixmap(pixmap)

        self.gridLayout.addWidget(self.img_label)

        self.info_label = QLabel(self)
        self.info_label.setObjectName(u"result_label")
        self.info_label.setWordWrap(True)

        self.gridLayout.addWidget(self.info_label, 0, Qt.AlignmentFlag.AlignLeft)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.info_label.setText("{}\nBy: {}\nDesc: {}".format(publish, channel, description))

        self.button = QPushButton(self)
        self.button.setObjectName(u"create_btn")
        self.button.setText("Generate Comment Stats")
        self.button.clicked.connect(self.get_comments)

        self.gridLayout.addWidget(self.button, 2, 0,  Qt.AlignmentFlag.AlignLeft)

        parent.verticalLayout_7.addWidget(self, 0, Qt.AlignmentFlag.AlignTop)


    @Slot()
    def get_comments(self):
        cmt_list = comments(self.container.youtube, self.id)['items']

        self.output = stat_output(self.container.youtube, cmt_list)
        self.output.show()

class stat_output(QWidget):
    def __init__(self, youtube, cmt_list) -> None:
        super().__init__()
        self.setWindowTitle("Stat Output")
        self.graphs = []
        self.cmts, self.cmt_ages, self.users, self.user_ages = from_comment(youtube, cmt_list)
        self.sent_df, sentiment_imgs = sentiment_stats(self.cmts)
        self.cmt_age_df, self.user_age_df, age_imgs = age_stats(self.cmt_ages, self.user_ages)
        self.gridLayout = QGridLayout(self)
        self.scrollList = QScrollArea(self)
        self.scrollList.setWidgetResizable(True)
        self.gridLayout.addWidget(self.scrollList)
        self.ScrollContents = QWidget()
        self.vertLayout = QVBoxLayout(self.ScrollContents)
        self.scrollList.setWidget(self.ScrollContents)
        self.ScrollContents.setLayout(self.vertLayout)
        pixmap = QPixmap()
        pixmap.load('image.png')
        self.saveOptions = QGroupBox(self)
        self.vertLayout.addWidget(self.saveOptions)
        self.saveLayout = QHBoxLayout()
        self.saveOptions.setLayout(self.saveLayout)

        self.savebtn = QPushButton(pixmap, "Save Selected", self)
        self.savebtn.clicked.connect(self.save_selected)
        self.saveLayout.addWidget(self.savebtn)

        self.sent_data = QCheckBox("Sentiment Raw DF", self)
        self.saveLayout.addWidget(self.sent_data)

        self.age_data = QCheckBox("Age Raw DF", self)
        self.saveLayout.addWidget(self.age_data)

        self.countLabel = QLabel(self)
        self.countLabel.setText(f"Comments Observed: {self.cmt_age_df.size}")
        self.saveLayout.addWidget(self.countLabel)

        for img in sentiment_imgs:
            self.graphs.append(graph(self, img))
        for img in age_imgs:
            self.graphs.append(graph(self, img))

    @Slot()
    def save_selected(self):
        folderName = QFileDialog.getExistingDirectory(self,
            "Choose a directory to save files", "/Documents")
        i = 0
        for graph in self.graphs:
            if graph.check.isChecked():
                graph.pixmap.save(folderName + '/fig_' + str(i), 'png')
                i+=1
        if self.sent_data.isChecked():
            np.save(folderName +"/sentiments.txt", self.sent_df)
        if self.age_data.isChecked():
            np.save(folderName +"/comment_ages.npy", self.cmt_age_df)
            np.save(folderName +"/user_ages.npy", self.user_age_df)

class graph(QWidget):
    def __init__(self, parent, image) -> None:
        super(graph, self).__init__()
        self.label = QLabel(self)
        self.check = QCheckBox(self)
        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.gridLayout.addWidget(self.label)
        self.gridLayout.addWidget(self.check)
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(image.read())
        self.label.setPixmap(self.pixmap)

        parent.vertLayout.addWidget(self, 0, Qt.AlignmentFlag.AlignTop)

if __name__ == '__main__':
    # make App and connect main window
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    ui = Ui_MainWindow()


    main_win.setWindowTitle("Sign in in Browser to Continue")
    ui.setupUi(main_win)
    main_win.show()
    main_win.setDisabled(True)
    
    ui.youtube = yt_auth()
    if not ui.youtube:
        main_win.close()
    main_win.setWindowTitle("Search for a Video!")
    main_win.setDisabled(False)
    
    sys.exit(app.exec())
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 
@Version: 
@Auther: XQING
@Date: 2019-11-03 21:13:11
@LastEditors: XQING
@LastEditTime: 2019-11-20 23:34:38
@Software: VSCode
'''

# import modules
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import sys
import news
import webbrowser
import requests
import time
import threading
import SentimentAnalysis as sa
import SearchSpotify as ss

# MainWindow Class
class MainWindow(QW.QWidget):
    '''
    init the MainWindow
    '''
    def __init__(self):
        super().__init__()
        self.initUi()

    # getNews Button's click event
    def getNewsBtn_click(self):
        def getNewsItem(title,description):
            '''
            The way of showing news in the nwesList
            layout
            -left news img
            -right_top news title
            -right_down news description
            '''
            # sometimes newsapi does not return a description for one piece of news
            if description == None:
                description = "No description for this"

            w = QW.QWidget()
            # layout
            layout_main = QW.QHBoxLayout()
            
            # news_pic = QW.QLabel()
            # news_pic.setFixedSize(50,30)
            # maps = QtGui.QPixmap().scaled(50,30)
            # news_pic.setPixmap(maps)
            TitleLabel = QW.QLabel(title)
            TitleLabel.setStyleSheet('font-size: 16px soild')
            TitleLabel.setWordWrap(True)
            DescriptionLabel = QW.QLabel(description)
            DescriptionLabel.setStyleSheet('font-size: 12px')
            DescriptionLabel.setWordWrap(True)

            layout_right = QW.QVBoxLayout()  # layout right
            layout_right.addWidget(TitleLabel)# title
            layout_right.addWidget(DescriptionLabel)  #  description
            
            #set the layout
            # layout_main.addWidget(news_pic)
            layout_main.addLayout(layout_right)
            w.setLayout(layout_main)
            return w
        
        # before start to get news disable self.displayTrackBtn.setEnabled(False)
        self.displayTrackBtn.setEnabled(False)
        #use news to get top headlines
        self.topHeadlines = news.getTopHeadlines()
        #keyWords = ['Jose Mourinho', 'passion', 'train', 'people', 'Ukraine pressure - Sondland', 'public duties', 'record-breaking explosion', "Hong Kong's university siege", 'Celeb', 'picture of Adele Roberts', 'cockpit', 'Boris Johnson', 'hunger strike', 'Hong Kong minister', 'manifesto pledge', 'Mother', 'dirt cheap FTSE', 'Samsung Galaxy S10 Lite', 'suspended animation', 'ways']
        keyWords = []
        self.trackInfo = []
        def getKeyWordAndTrackInfo():
            for i in self.topHeadlines['articles']:
                keyWords.append(sa.key_phrases(i['title']))
            time.sleep(2)
            for j in keyWords:
                self.trackInfo.append(ss.getSong(j))
            
            self.displayTrackBtn.setEnabled(True)
            print(keyWords)
            print(self.trackInfo)
        t1 = threading.Thread(target=getKeyWordAndTrackInfo,name="getKeyWordAndTrackInfo")
        t1.start()

        sentime = 0
        def getSentime():
            sentime = sa.sentiment(keyWords)
            print(sentime)
        t2 = threading.Thread(target=getSentime,name="getSentime")
        t2.start()
        
        for i in self.topHeadlines['articles']:
            #self.newsList.addItem(i['title'])
            print(i['title'],i['description'],i['urlToImage'])
            item = QW.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(200,100))
            w = getNewsItem(i['title'],i['description'])
            self.newsList.addItem(item)
            self.newsList.setItemWidget(item,w)
          
    def displayTrack_click(self):
        
        def getSpotifyItem(name,artist):
            w = QW.QWidget()
            layout_main = QW.QHBoxLayout()

            trackNameLabel = QW.QLabel(name)
            trackNameLabel.setStyleSheet('font-size: 16px soild')
            trackNameLabel.setWordWrap(True)
            artistLabel = QW.QLabel(artist)
            artistLabel.setStyleSheet('font-size: 12px')
            artistLabel.setWordWrap(True)
            layout_list = QW.QVBoxLayout()
            layout_list.addWidget(trackNameLabel)# track name
            layout_list.addWidget(artistLabel)  #  track artist
            layout_main.addLayout(layout_list)
            w.setLayout(layout_main)
            print('return W')
            return w
        track = []
        for k in self.trackInfo:
            if k != 'Error' and 'None':
                track.append(k)
        self.trackInfo = track
        for i in self.trackInfo:
            item = QW.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(150,100))
            w = getSpotifyItem(i['name'],i['artist'])
            self.songList.addItem(item)
            self.songList.setItemWidget(item,w)

    def aboutBtn_click(self):
        QW.QMessageBox.information(self,"About our group","Group Info",QW.QMessageBox.Yes)

    def clickNews(self,item):
        webbrowser.open(self.topHeadlines['articles'][self.newsList.currentRow()]['url'])
        
    def cilckTrack(self,item):
        url  = self.trackInfo[self.songList.currentRow()]['url']
        if url != None:
            webbrowser.open(url)
        
    
    def initUi(self):
        # set the MainWindow
        self.setWindowTitle("Spotify&News")
        self.resize(1200,600)
        self.setMinimumSize(750,500)
        # self.setFixedSize(800,500) # set the window at a fixed size
        # set the windows show in the middle of screen
        screen = QW.QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft,newTop)
        # button getNews
        self.getNewsBtn = QW.QPushButton('Get News',self)
        self.getNewsBtn.clicked.connect(self.getNewsBtn_click)
        # button about
        self.aboutBtn = QW.QPushButton('About',self)
        self.aboutBtn.clicked.connect(self.aboutBtn_click)
        # buton display tracks
        self.displayTrackBtn =QW.QPushButton('Dsiplay Tracks',self)
        self.displayTrackBtn.setEnabled(False)
        self.displayTrackBtn.clicked.connect(self.displayTrack_click)
        # Spotify song list
        self.songList = QW.QListWidget(self)
        self.songList.itemClicked.connect(self.cilckTrack)    
        # news list
        self.newsList = QW.QListWidget(self)
        self.newsList.itemClicked.connect(self.clickNews)
        # ui layout
        hbox = QW.QHBoxLayout()

        hbox.addWidget(self.songList,stretch=2)

        hbox.addWidget(self.newsList,stretch=8)

        btnbox = QW.QHBoxLayout()
        btnbox.addWidget(self.aboutBtn)
        btnbox.addWidget(self.displayTrackBtn)
        btnbox.addWidget(self.getNewsBtn)
        
        vbox = QW.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(btnbox)
        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    w = MainWindow()
    app.exit(app.exec_())
    
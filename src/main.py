#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 
@Version: 
@Auther: XQING
@Date: 2019-11-03 21:13:11
@LastEditors: XQING
@LastEditTime: 2019-11-12 15:05:37
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
import SearchSpotify
from PIL import Image

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
            w = QW.QWidget()
            # layout
            layout_main = QW.QHBoxLayout()
            
            news_pic = QW.QLabel()
            news_pic.setFixedSize(50,30)
            maps = QtGui.QPixmap().scaled(50,30)
            news_pic.setPixmap(maps)

            layout_right = QW.QVBoxLayout()  # layout right
            layout_right.addWidget(QW.QLabel(title))  # title
            layout_right.addWidget(QW.QLabel(description))  #  description
            #set the layout
            layout_main.addWidget(news_pic)
            layout_main.addLayout(layout_right)
            w.setLayout(layout_main)
            return w
        
        #use news to get top headlines
        self.topHeadlines = news.getTopHeadlines()
        for i in self.topHeadlines['articles']:
            #self.newsList.addItem(i['title'])
            #print(i['title'],i['description'],i['urlToImage'])
            item = QW.QListWidgetItem()
            
            item.setSizeHint(QtCore.QSize(200,100))
            
            
            
            w = getNewsItem(i['title'],i['description'])
            self.newsList.addItem(item)
            self.newsList.setItemWidget(item,w)
    

    def clickNews(self,item):
        webbrowser.open(self.topHeadlines['articles'][self.newsList.currentRow()]['url'])
        
        
    def initUi(self):
        # set the MainWindow
        self.setWindowTitle("Spotify&News")
        self.resize(1200,600)
        self.setFixedSize(1200,600)
        # set the windows show in the middle of screen
        screen = QW.QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft,newTop)
        # button getNews
        self.getNewsBtn = QW.QPushButton('Get News',self)
        self.getNewsBtn.clicked.connect(self.getNewsBtn_click)
        # Spotify song list
        self.songList = QW.QListWidget(self)      
        # news list
        self.newsList = QW.QListWidget(self)
        self.newsList.itemClicked.connect(self.clickNews)
        # ui layout
        hbox = QW.QHBoxLayout()

        hbox.addWidget(self.songList,stretch=2)

        hbox.addWidget(self.newsList,stretch=8)

        vbox = QW.QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.getNewsBtn)
        
        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    w = MainWindow()
    app.exit(app.exec_())
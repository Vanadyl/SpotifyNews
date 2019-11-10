#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 
@Version: 
@Auther: XQING
@Date: 2019-11-03 21:13:11
@LastEditors: XQING
@LastEditTime: 2019-11-10 07:27:03
@Software: VSCode
'''


import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import sys
import news
import webbrowser
import requests
from PIL import Image

class MainWindow(QW.QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def getNewsBtn_click(self):
        def getNewsItem(title,description,img):
            # Widget for news item
            w = QW.QWidget()
            # layout
            layout_main = QW.QHBoxLayout()
            
            news_pic = QW.QLabel()
            news_pic.setFixedSize(50,30)
            maps = QtGui.QPixmap(img).scaled(50,30)
            news_pic.setPixmap(maps)

            layout_right = QW.QVBoxLayout()  # layout right
            layout_right.addWidget(QW.QLabel(title))  # title
            layout_right.addWidget(QW.QLabel(description))  #  description

            layout_main.addWidget(news_pic)
            layout_main.addLayout(layout_right)
            w.setLayout(layout_main)
            return w
        
        
        self.topHeadlines = news.getTopHeadlines()
        for i in self.topHeadlines['articles']:
            #self.newsList.addItem(i['title'])
            #print(i['title'],i['description'],i['urlToImage'])
            item = QW.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(200,50))
            
            img = Image.open(r'C:\Users\19218\Desktop\SpotifyNews\src\lhd_sing.png')
            
            w = getNewsItem(i['title'],i['description'],img)
            self.newsList.addItem(item)
            self.newsList.setItemWidget(item,w)
    

    def clickNews(self,item):
        webbrowser.open(self.topHeadlines['articles'][self.newsList.currentRow()]['url'])
        
        
    def initUi(self):
        self.setGeometry(300,500,500,500)
        self.setWindowTitle("Spotify&News")
        #button getNews
        self.getNewsBtn = QW.QPushButton('Get News',self)
        self.getNewsBtn.clicked.connect(self.getNewsBtn_click)
        #news list
        self.newsList = QW.QListWidget(self)
        self.newsList.itemClicked.connect(self.clickNews)

        #ui layout
        hbox = QW.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.getNewsBtn)
        
        vbox = QW.QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addWidget(self.newsList)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()

if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    w = MainWindow()
    app.exit(app.exec_())
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Description: 
@Version: 
@Auther: XQING
@Date: 2019-11-03 21:21:04
@LastEditors: XQING
@LastEditTime: 2019-11-10 02:54:59
@Software: VSCode
'''



import json
from newsapi import NewsApiClient

# newsapi Object
newsapi = NewsApiClient(api_key='ff70da1046ce43e6a345d0ac2fcd4493')


def getTopHeadlines(country='gb', page=1, page_size=20):
    """
    get top headlines of GB
    parameter country, category, sources can not exists in the same time
    pagesize default is 20
    """
    top_headlines = newsapi.get_top_headlines(country=country, page=page, page_size=page_size)
    
    if top_headlines['status'] == 'ok':
        return top_headlines
    else:
        return 'error'


def test():
    print()




if __name__ == '__main__':
    test()


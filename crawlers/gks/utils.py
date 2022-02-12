#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from unidecode import unidecode
import datetime 

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def parse_korea_embassy_data(data, urls, dates):
    for i, text in enumerate(data):
        text = unidecode(text).lower()
        logger.info(text)
        matches = re.search('gks', text)
        url = parse_korea_embassy_url(urls[i])
        news_date = dates[i]
        news_date = datetime.datetime.strptime(news_date, r'%Y-%m-%d').date()
        today = datetime.date.today()

        if matches and today <= news_date:

            return text, None, url, news_date


def parse_korea_embassy_url(text):
    logger.info(text)
    text = unidecode(text)
    url = 'https://overseas.mofa.go.kr/br-pt/brd/m_22116/view.do?seq=%s&page=1'
    news_number = re.search(r"\('(\d*)'\)", text).group(1)
    url = url % (news_number)
    logger.info(url)
    
    return url

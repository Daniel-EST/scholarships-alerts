#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
from unidecode import unidecode

from bs4 import BeautifulSoup

logger = logging.getLogger()
logger.setLevel(logging.INFO)

KOREAN_EMBASSY_URL = 'https://overseas.mofa.go.kr/br-pt/brd/m_22116/list.do'


def request_korea_embassy_news_data():
    r = requests.get(KOREAN_EMBASSY_URL)
    logger.info(f'{r.status_code}')
    soup = BeautifulSoup(r.text, 'html.parser')

    selection = soup.select('.al a')
    data = [unidecode(program.get_text()) for program in selection] 
    urls = [program['onclick'] for program in selection] 

    dates_selection =  soup.select('tr > td:nth-child(4)')
    news_dates = [unidecode(date.get_text()) for date in dates_selection] 

    return data, urls, news_dates

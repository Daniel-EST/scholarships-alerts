#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
from unidecode import unidecode

from bs4 import BeautifulSoup

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CHINESE_EMBASSY_URL = 'http://br.china-embassy.org/por/sghds/'

HEADERS = {
    'User-Agent': """Mozilla/5.0 (Windows NT 10.0; Win64; x64)""",
    'Cache - Control': 'no-cache',
    'Content-Type': 'text/html; charset=utf-8'
}

def request_chinese_embassy_news_data():
    r = requests.get(CHINESE_EMBASSY_URL, headers=HEADERS)
    logger.info(f'{r.status_code}')
    soup = BeautifulSoup(r.text, 'html.parser')
    selection = soup.select('#docMore .middle_ct li')
    data = [unidecode(program.get_text()) for program in selection] 
    selection = soup.select('#docMore .middle_ct li a')
    urls = [program['href'] for program in selection]

    return data, urls

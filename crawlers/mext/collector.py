#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging

from bs4 import BeautifulSoup



logger = logging.getLogger()
logger.setLevel(logging.INFO)

MEXT_URL = 'https://www.br.emb-japan.go.jp/itpr_pt/bolsas_programas.html'

HEADERS = {
    'User-Agent': """Mozilla/5.0 (Windows NT 10.0; Win64; x64)""",
    'Cache - Control': 'no-cache',
    'Content-Type': 'text/html; charset=utf-8'
}

def request_mext_data():
    r = requests.get(MEXT_URL, headers=HEADERS)
    logger.info(f'{r.status_code}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')

        data = [program.get_text() for program in soup.select('#coluna-direita .linklist li')]
        urls = [program['href'] for program in soup.select('#coluna-direita .linklist li a')]
        news_date = [program.get_text()  for program in soup.select('#main .rightalign')]
        news_date = news_date[0]

        return data, urls, news_date
        
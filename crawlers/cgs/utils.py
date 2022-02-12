#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from unidecode import unidecode

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def parse_chinese_embassy_data(data, urls):
    for i, text in enumerate(data):
        text = unidecode(text).lower()
        pattern = r'programa de bolsa'
        matches = re.match(pattern, text)
        url = urls[i]

        if matches:
            text = text.replace('chinaas', 'chinês')
            year = re.search("\d{4}-\d{4}", text).group(0)
            news_date = re.search("\d{4}-\d{2}-\d{2}", text).group(0)

            return text, year, url, news_date


def parse_chinese_embassy_program_results_data(data, urls):
    for i, text in enumerate(data):
        text = unidecode(text).lower()
        pattern = r'resultado da sele'
        matches = re.match(pattern, text)
        url = urls[i]

        if matches:
            text = text.replace('chinaas', 'chinês')
            year = re.search("\d{4}-\d{4}", text).group(0)
            news_date = re.search("\d{4}-\d{2}-\d{2}", text).group(0)

            return text, year, url, news_date
            

def parse_chinese_embassy_url(text):
    text = unidecode(text)
    pattern = r'http://br.china-embassy.org/por/sghds'
    matches = re.match(pattern, text)

    if not matches:
        url = f'{pattern}{text[1:]}'
    else:
        url = text
    
    return url

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from unidecode import unidecode
from datetime import datetime


MONTHS = {
    'janeiro': 1,
    'fevereiro': 2,
    'marco' : 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12
}


def parse_mext_data(data):
    programs = list()
    dates = list()
    for text in data:
        text = unidecode(text)
        pattern = r'(.*) \((inscricoes.*)\)'
        matches = re.search(pattern, text)
        if matches:
            program = matches.group(1)
            date = matches.group(2)

            programs.append(program)
            dates.append(date)
            
    return programs, dates


def parse_mext_date(text):
    text = unidecode(text)
    pattern = r'(\d{1,2}) de (\w+) a (\d{1,2}) de (\w+) de (\d{4})'
    pattern2 = r'(\d{1,2}) a (\d{1,2}) de (\w+) de (\d{4})'
    matches = re.search(pattern, text)
    matches2 = re.search(pattern2, text)

    if matches:
        day_init = int(matches.group(1))
        month_init = MONTHS[matches.group(2)]
        day_end = int(matches.group(3))
        month_end = MONTHS[matches.group(4)]
        year = int(matches.group(5))

        start = datetime(year, month_init, day_init)
        end = datetime(year, month_end, day_end)
    
    elif matches2:
        day_init = int(matches2.group(1))
        month_init = MONTHS[matches2.group(3)]
        day_end = int(matches2.group(2))
        month_end = MONTHS[matches2.group(3)]
        year = int(matches2.group(4))

        start = datetime(year, month_init, day_init)
        end = datetime(year, month_end, day_end)

    elif text=='inscricoes encerradas':
        start = None
        end = None

    dates =  {
        'start_date': start, 
        'end_date': end
    }
    
    return dates

def parse_mext_dates(texts):
    dates = list()
    for text in texts:
        dates.append(parse_mext_date(text))

    return dates

def parse_mext_url(text):
    text = unidecode(text)
    pattern = r'https://www.br.emb-japan.go.jp'
    matches = re.match(pattern, text)

    if not matches:
        url = f'{pattern}{text}'
        
    else:
        url = text
    
    return url

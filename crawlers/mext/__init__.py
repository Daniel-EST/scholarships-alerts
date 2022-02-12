#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .collector import request_mext_data
from .utils import (
    parse_mext_data,
    parse_mext_dates,
    parse_mext_url
)

import datetime
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

AVAILABLE_PROGRAMS = {
    'research': 'Pesquisa',
    'research': 'Pesquisa',
    'research': 'Pesquisa',
    'research': 'Pesquisa',
    'research': 'Pesquisa',
    'research': 'Pesquisa',
    'research': 'Pesquisa',
    'research': 'Pesquisa'
}

PROGRAM_CODES = {
    'Pesquisa': 1,
    'Pesquisa': 1,
    'Pesquisa': 1,
    'Pesquisa': 1,
    'Pesquisa': 1,
    'Pesquisa': 1,
    'Pesquisa': 1,
    'Pesquisa': 1
}

class Mext(object):

    def __init__(self):
        self.__name = 'MEXT'
        self.__country = 'Japan'
        self.__availabe_programs = AVAILABLE_PROGRAMS.keys()

    
    def get_program(self, program='research'):
        if str(program) not in self.__availabe_programs:
            return ''

        data = self.get_programs()
        return data['program']

    def get_programs(self):
        data, urls, news_date = request_mext_data()
        logger.info(f'{data}, {urls}, {news_date}')

        news_date = datetime.datetime.strptime(news_date, r'%Y/%m/%d').date()
        today = datetime.date.today()

        if today <= news_date:
            programs, dates = parse_mext_data(data)
            logger.info(f'{programs}, {dates}, {news_date}')
            
            dates = parse_mext_dates(dates)
            logger.info(f'{dates}')

            data = []
            this_year = today.year
            next_year = this_year + 1

            for i, program in enumerate(programs):
                date = dates[i]
                url = urls[i]
                url = parse_mext_url(url)
                program_data = {
                        'program': program,
                        'name': self.__name,
                        'country': self.__country,
                        'register_period': date,
                        'url': url,
                        'year': f'{this_year}-{next_year}'
                    }
                data.append(program_data)

            return data

        
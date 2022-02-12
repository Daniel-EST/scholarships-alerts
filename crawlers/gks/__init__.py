#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .collector import request_korea_embassy_news_data
from .utils import parse_korea_embassy_data

import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Gks(object):

    def __init__(self):
        self.__name = 'GKS'
        self.__country = 'Korea'
    
    def get_program(self):
        data, urls, news_dates = request_korea_embassy_news_data()
        logger.info(f'{data}, {urls}, {news_dates}')
        
        program, date, url, news_date = parse_korea_embassy_data(data, urls, news_dates)
        logger.info(f'{program}, {date}, {url}, {news_date}')


        logger.info(f'## Returning GKS')
        data =  {
            'name': self.__name,
            'program': program,
            'country': self.__country,
            'register_period': {'start_date': datetime.date.today(), 'end_date': datetime.date.today()},
            'url': url,
            'year': date
        }
        logger.info(data)
        return data

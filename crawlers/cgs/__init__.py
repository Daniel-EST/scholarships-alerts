#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .collector import request_chinese_embassy_news_data
from .utils import (
    parse_chinese_embassy_data,
    parse_chinese_embassy_url,
    parse_chinese_embassy_program_results_data
)

import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Cgs(object):

    def __init__(self):
        self.__name = 'CGS'
        self.__country = 'China'
    
    def get_program(self):
        data, urls = request_chinese_embassy_news_data()
        logger.info(f'{data}, {urls}')
        
        program, date, url, news_date = parse_chinese_embassy_data(data, urls)
        logger.info(f'{program}, {date}, {url}, {news_date}')
        
        url = parse_chinese_embassy_url(url)
        logger.info(f'{url}')

        news_date = datetime.datetime.strptime(news_date, r'%Y-%m-%d').date()
        today = datetime.date.today()

        if today <= news_date:
            logger.info(f'## Returning CGS')
            url = parse_chinese_embassy_url(url)

            return {
                'name': self.__name,
                'program': program,
                'country': self.__country,
                'register_period': {'start_date': datetime.date.today(), 'end_date': datetime.date.today()},
                'url': url,
                'year': date
            }


    def get_lastest_results(self):
        data, urls = request_chinese_embassy_news_data()
        program, date, url, news_date = parse_chinese_embassy_program_results_data(data, urls)
        
        news_date = datetime.datetime.strptime(news_date, r'%Y-%m-%d').date()
        today = datetime.date.today()

        if today <= news_date:
            url = parse_chinese_embassy_url(url)

            return {
                'name': self.__name,
                'program': program,
                'country': self.__country,
                'register_period': {'start_date': datetime.date.today(), 'end_date': datetime.date.today()},
                'url': url,
                'year': date
            }

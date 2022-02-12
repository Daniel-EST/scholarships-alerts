#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from start_crawler import start_crawler_and_alert

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, lambda_context):
    logger.info('## Lambda handler invoked')
    start_crawler_and_alert()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

import alert.email
import alert.telegram
from crawlers.cgs import Cgs
from crawlers.mext import Mext
from crawlers.gks import Gks

logger = logging.getLogger()
logger.setLevel(logging.INFO)

EMAIL_RECEIVE_1=os.environ.get('EMAIL_RECEIVE_1')
EMAIL_RECEIVE_2=os.environ.get('EMAIL_RECEIVE_2')

def start_crawler_and_alert():
    cgs = Cgs()
    mext = Mext()
    gks = Gks()
    
    logger.info(f'## Crawling started')

    try:
        logger.info(f'## MEXT Data')
        mext_programs = mext.get_programs()
        logger.info(f'{mext_programs}')
        
        logger.info(f'## Sending emails')
        for program in mext_programs:
            logger.info(f'Program: {program}')
            
            if program['register_period']['start_date'] != None:
                logger.info(f'Sending: {program}')
                alert.email.send_emails(program, [EMAIL_RECEIVE_1, EMAIL_RECEIVE_2])
                alert.telegram.send_message(program)

    except Exception as e:
        logger.info(f'Error MEXT')
        logger.info(e)
    
    try:
        logger.info(f'## CGS Data')
        cgs_program = cgs.get_program()
        logger.info(f'Program: {cgs_program}')
        logger.info(f'## Sending emails')
        alert.email.send_emails(cgs_program, [EMAIL_RECEIVE_1, EMAIL_RECEIVE_2])
        alert.telegram.send_message(cgs_program)

    except Exception as e:
        logger.info(f'Error CGS')
        logger.info(e)

    try:
        logger.info(f'## GKS Data')
        gks_program = gks.get_program()
        logger.info(f'Program: {gks_program}')
        logger.info(f'## Sending emails')
        alert.email.send_emails(gks_program, [EMAIL_RECEIVE_1, EMAIL_RECEIVE_2])
        alert.telegram.send_message(gks_program)

    except Exception as e:
        logger.info(f'Error GKS')
        logger.info(e)
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib, ssl
import os
import time
import logging

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger()
logger.setLevel(logging.INFO)


EMAIL=os.environ.get('EMAIL')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')

PORT = 465 

def send_emails(data, receivers):
    context = ssl.create_default_context()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Inscrições do {data["name"]} abertas!'
    msg['From'] = EMAIL

    text = f'Olá,\nAparentemente as inscrições do {data["name"]} para {data["program"]} já estão abertas!\nEntre no site do {data["name"]} e saiba mais!'
    html =  f"""\
    <html>
    <head></head>
    <body>
        <p> Olá, <br>
        Aparentemente as inscrições do <b>{data["name"]}</b> para <b>{data["program"]}</b> já estão abertas!<br>
        Entre no site do <a href="{data["url"]}">{data["name"]}<a> e saiba mais!
        </p><br>
        Se o link acima não funcionar, utilize a url abaixo:<br>
        <a href="{data["url"]}">{data["url"]}<a>
    </body>
    </html>
    """

    plain_part = MIMEText(text, 'plain')
    html_part = MIMEText(html, 'html')

    msg.attach(plain_part)
    msg.attach(html_part)

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        for receiver in receivers:
            logger.info(receiver)
            try:
                server.sendmail(EMAIL, receiver, msg.as_string())
            except Exception as e: 
                logger.info(e)
                
            time.sleep(0.1)

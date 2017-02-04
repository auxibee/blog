#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alinko-pc
#
# Created:     26/01/2017
# Copyright:   (c) alinko-pc 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask_mail import Message
from app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject=subject , sender=sender, recipients=recipients )
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
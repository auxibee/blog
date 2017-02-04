#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alinko-pc
#
# Created:     21/01/2017
# Copyright:   (c) alinko-pc 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = "hdie3399dflkhkhkdseiad"

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True

#slow database query threshold
DATABASE_QUERY_TIMEOUT = 0.5

#email token key
TOKEN_KEY = 'UAhsbbbUGGGsbcc'
TOKEN_PASS = 'DFAHhdfaafdaadf'

#mail settings
MAIL_SERVER = 'stmp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TSL = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'yaw217'
MAIL_PASSWORD = '217317auxi'
ADMINS = ['yaw217@gmail.com']

POSTS_PER_PAGE = 15
MAX_SEARCH_RESULTS = 20

CATEGORIES = ['general_news','relationship','entertainment','soccer',
                'business','politics','leak','programming',
                'music','jokes','music','education',
                'nurse','news','tennis','scam',
                'mtn','tigo','committee']

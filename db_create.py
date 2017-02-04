#!flask/bin/python
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

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db

import os.path

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO,'database_repository')
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO,api.version(SQLALCHEMY_MIGRATE_REPO))



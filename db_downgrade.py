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
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alinko-pc
#
# Created:     27/01/2017
# Copyright:   (c) alinko-pc 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------



from itsdangerous import URLSafeTimedSerializer
from config import TOKEN_KEY,TOKEN_PASS

def generate_token(email):
   serializer = URLSafeTimedSerializer(TOKEN_KEY)
   return serializer.dumps(email,salt=TOKEN_PASS)

def confirm_token(token,expiration=3600):
    serializer = URLSafeTimedSerializer(TOKEN_KEY)
    try:
        email = serializer.loads(token,TOKEN_PASS,max_age=expiration)
    except:
        return False
    return email
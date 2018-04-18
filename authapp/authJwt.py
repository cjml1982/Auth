from datetime import datetime,timedelta
import jwt
import time
import base64
from Crypto.PublicKey import RSA
import json
import logging
#from django.conf import settings #get JWT_EXP_DELTA_SECONDS from the settings file

logger= logging.getLogger("django")

JWT_SECRET="!QAZ@WSX#EDC$RFV%TGB6yhn7ujm8ik,"
JWT_ALGORITHM='HS256'
JWT_EXP_DELTA_SECONDS = 604800 #7days

def create_jwt(usertemp):
    logger.info("Enter function create_jwt,user=%s",usertemp)
    jwt_token = None
    #payload={
        #'iss':"Earthledger AUTH",
        #'exp':datetime.utcnow()+timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        #'username':usertemp,
    #}
    try:
        payload={
            'iss':"Earthledger AUTH",
            'iat':datetime.utcnow(),
            'exp':datetime.utcnow()+timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            'username':usertemp,
        }
    
        jwt_token=jwt.encode(payload,JWT_SECRET,JWT_ALGORITHM)
    except Exception, e:
        logger.error(e)
    
    return jwt_token


def verify_jwt(usertemp,jwt_token):
    logger.info("Enter function verify_jwt,user=%s",usertemp)
    result = False
    try:
        received_payload = jwt.decode(jwt_token,JWT_SECRET,algorithms=[JWT_ALGORITHM])
         
    except Exception,e:
        logger.error(e)
        return result

    jwtexp=received_payload.get('exp')

    currenttime = datetime.utcnow() #currenttime is datetime type
    ct = int(time.mktime(currenttime.timetuple())) #time.mktime return float type, timetuple is 9-item time structure

    #if 
    if usertemp == received_payload["username"]:
        if ct >jwtexp: # if jwt expired
            result = 'expired'
        else:
            result = True
    else:
        result = 'unAuth'

    return result


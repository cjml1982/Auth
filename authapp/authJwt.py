from datetime import datetime,timedelta
import jwt
import base64
from Crypto.PublicKey import RSA
import json

JWT_SECRET="!QAZ@WSX#EDC$RFV%TGB6yhn7ujm8ik,"
JWT_ALGORITHM='HS256'
JWT_EXP_DELTA_SECONDS = 2000

def create_jwt(usertemp):
    print usertemp
    jwt_token = None
    #payload={
        #'iss':"Earthledger AUTH",
        #'exp':datetime.utcnow()+timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        #'username':usertemp,
    #}
    try:
        payload={
            'iss':"Earthledger AUTH",
            'exp':datetime.utcnow()+timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            'username':usertemp,
        }
        print payload
    
        jwt_token=jwt.encode(payload,JWT_SECRET,JWT_ALGORITHM)
        #json_token=jwt_token.decode('utf-8')
        print jwt_token
    except Exception, e:
        print e
        return jwt_token
    
    #if None == jwt_token:
        #return None
    return jwt_token


def verify_jwt(usertemp,jwt_token):
    result = False
    try:
        received_payload = jwt.decode(jwt_token,JWT_SECRET,algorithms=[JWT_ALGORITHM])
        print received_payload
        if usertemp == received_payload["username"]:
            result = True
    except Exception,e:
        print e
        return result
    return result




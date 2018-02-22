import jwt
import base64
from Crypto.PublicKey import RSA
import json
from datetime import datetime,timedelta

JWT_SECRET = "!QAZ@WSX#EDC$RFV%TGB6yhn7ujm8ik,"
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 2000
usertemp = "yilian333"

payload={
    'iss':"Earthledger AUTH",
    'exp':datetime.utcnow()+timedelta(seconds=JWT_EXP_DELTA_SECONDS),
    'username':usertemp,
}
print payload

#with open('master-private.pem','rb') as f:
#    signing_key=jwk_from_pem(f.read())
try:
    jwt_token = jwt.encode(payload,JWT_SECRET,JWT_ALGORITHM)
    #jwt_token
except Exception, e:
    print e

json_token= jwt_token.decode('utf-8')

print json_token

#compact_jwt=jwt.encode(message,signing_key,'RS256')

#with open('master-public.pem','r') as f:
#    verifying_key = jwk_from_pem(f.read())

message_received = jwt.decode(jwt_token,JWT_SECRET,algorithms=[JWT_ALGORITHM])

print message_received

#assert message== message_received


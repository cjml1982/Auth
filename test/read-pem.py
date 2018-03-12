from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

'''
data_file = open("data.bin", 'rb')
data = data_file.read()
data_file.close()
'''

pri_key_file = open("master-private.pem", 'rb')
pri_key_data = pri_key_file.read()
pri_key_file.close()

pub_key_file = open("master-public.pem", 'rb')
pub_key_data = pub_key_file.read()
pub_key_file.close()

pub_pkcs1_key_file = open("master-public-pkcs1.pem", 'rb')
pub_pkcs1_key_data = pub_pkcs1_key_file.read()
pub_pkcs1_key_file.close()


pri_pkcs8_key_file = open("master-private-pkcs8.pem", 'rb')
pri_pkcs8_key_data = pri_pkcs8_key_file.read()
pri_pkcs8_key_file.close()


pri = base64.b64encode(pri_key_data)
pub = base64.b64encode(pub_key_data)
pri_pkcs8 = base64.b64encode(pri_pkcs8_key_data)
pub_pkcs1 = base64.b64encode(pub_pkcs1_key_data)

print "privateKey"
print pri
print "publicKey"
print pub
print "privatePkcs8Key"
print pri_pkcs8
print "publik pkcs1 key"
print pub_pkcs1


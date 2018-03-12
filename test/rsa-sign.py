import base64
import hashlib
import rsa
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from Crypto.Hash import SHA


'''
signKeyModHex  = "cc8e3eb61179e5257ea3adaa3329a49f1ac1776f8d52081c01208b1e70c8251e919e217cc31da5f4faee2b87fa4129b9f26a8127c565345b8a078356d59d3594202afc9e97a131a8d9a94196f0f8b397d5ff1c98b2a2a12fca8696409259507cf841193bed7e69469909b1061a0bd2fb42ae43beef8600b1312a2e36d9127f95"  
signKeyExpHex  = "ed7673f6887329404db35577afcd37fe3be13bf593e916e0ebae0bd25abafddc6ecf53b0b21149070c06512299b1ebeea12c62a2f8d473e39069085f55bc1ae4b69058ddee5d96e4ee5fd90a9f42b7b8fc4e6b096d08a55a8e643091294bd680e5d2dd8ff599f17a2883ccf63fe69b474467c539de6709609c9bc4cd36c8121"  
  
n = int(signKeyModHex,16)  
d = int(signKeyExpHex,16)  
sign_str = "123456"  
  
# method1:
# rsa.key.PrivateKey proto: def __init__(self, n, e, d, p, q, exp1=None, exp2=None, coef=None):  
# when coef is null, p and q can't be 0; coef=1, p and q can be 0. because only n and d are know
privatekey = rsa.key.PrivateKey(n,0,d,0,0,coef=1)

#mothod2:  
impl = RSA.RSAImplementation(use_fast_math=False)  
privatekey = impl.construct((n, 0))  
privatekey.key.d = d  
'''
'''
(pubkey,privkey) = rsa.newkeys(1024)
with open('public.pem','w+') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('private.pem','w+') as f:
    f.write(privkey.save_pkcs1().decode())

with open('public.pem','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem','r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
'''
  
# method3(load PKCS#1):
with open('master-private.pem', 'rb') as privatefile:  
    keydata = privatefile.read()  
privatekey = rsa.PrivateKey.load_pkcs1(keydata)  


sign_str ="58609"  
  
# rsa sign 
signature = rsa.sign(sign_str.encode('utf-8'), privatekey, 'SHA-1')  
signature_base64 = base64.b64encode(signature).decode('utf-8')  
   
#print(signature)  
print(signature_base64)  

#use lib rsa
#rsa load key with format pkcs1
with open('master-public-pkcs1.pem', 'rb') as publicfile:
    keydata_pub = publicfile.read()
publickey = rsa.PublicKey.load_pkcs1(keydata_pub)

print rsa.verify(sign_str.encode('utf-8'),signature,publickey)



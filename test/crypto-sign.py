from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from Crypto.Hash import SHA


with open('master-private-pkcs8.pem','r') as f:
    private_pem=f.read()

message = "62077"

privatekey = RSA.importKey(private_pem)

signer = Signature_pkcs1_v1_5.new(privatekey)

digest = SHA.new()
digest.update(message)
sign = signer.sign(digest)
print sign
signature = base64.b64encode(sign)

print signature

#rsaSign= base64.b64decode(signtemp)
#print rsaSign
#pubkey_dict= models.Publickey.objects.get(user=usertemp)
with open('master-public.pem','r') as f:
     pubkey_pem=f.read()
        #pubkey_pem = base64.b64decode(pubkey_dict.key)
print pubkey_pem
rsakey = RSA.importKey(pubkey_pem)
verifier = Signature_pkcs1_v1_5.new(rsakey)
digest = SHA.new()

digest.update(message)
is_verify=verifier.verify(digest,base64.b64decode(signature))
print is_verify

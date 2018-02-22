from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

message ="9002"
with open('master-private.pem','r') as f:
    key = f.read()
rsakey=RSA.importKey(key)
signer=Signature_pkcs1_v1_5.new(rsakey)
digest = SHA.new()
digest.update(message)
print digest.hexdigest()
sign = signer.sign(digest)
signature_old = base64.b64encode(sign)
print signature_old
signature_new=signature_old.replace("+","%2B")

print signature_new

with open('master-public.pem','r') as f:
    key = f.read()
rsakey = RSA.importKey(key)
verifier = Signature_pkcs1_v1_5.new(rsakey)
digest = SHA.new()
digest.update(message)
is_verify = verifier.verify(digest, base64.b64decode(signature_old))
print is_verify

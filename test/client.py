from Crypto import Random
from Crypto.PublicKey import RSA
import base64


#generate random 
random_generator = Random.new().read

#rsa
rsa = RSA.generate(1024,random_generator)

#export the key to master
private_pem=rsa.exportKey()

with open('master-private.pem','wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()

with open('master-public.pem','wb') as f:
    f.write(public_pem)

#ghost the key
with open('ghost-private.pem','wb') as f:
    f.write(private_pem)

with open('ghost-public.pem','wb') as f:
    f.write(public_pem)

print private_pem

print public_pem

private_pem_b64 = base64.b64encode(private_pem)

public_pem_b64 = base64.b64encode(public_pem)


print private_pem_b64

print public_pem_b64


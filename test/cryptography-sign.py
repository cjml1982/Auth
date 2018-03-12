from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

data_file = open("data.bin", 'rb')
data = data_file.read()
data_file.close()

key_file = open("master-private.pem", 'rb')
key_data = key_file.read()
key_file.close()

private_key = serialization.load_pem_private_key(
    key_data,
    password=None,
    backend=default_backend()
)

signature = private_key.sign(
    data,
    padding.PKCS1v15(),
    hashes.SHA256()
)

signature_file = open("data.sig", 'wb')
signature_file.write(signature)
signature_file.close()

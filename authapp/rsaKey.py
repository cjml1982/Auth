
from Crypto.PublicKey import RSA  # pkcs8 sign and verify
from Crypto.Hash import SHA
from authapp import models
import base64
import rsa  # pkcs1  sign,and verify
from rsa._compat import b,is_bytes
import logging

logger= logging.getLogger("django")

def checkKeyFormat(usertemp,pubkey):
    logger.info("Enter function checkKeyFormat,user= %s",usertemp)
    try:
        pubkey_pem = base64.b64decode(pubkey) # transfer base64 to pem format

        format = checkPublicKeyFormat(pubkey_pem)
        logger.info("user %s's public key format is %s",usertemp,format)

        if ("pkcs1" == format):
            pkcs1rsakey = rsa.PublicKey.load_pkcs1(pubkey_pem)
        elif ("pkcs8" == format):
            rsakey= RSA.importKey(pubkey_pem)
        else:
            return False
    except Exception,e:
        logger.error(e)
        return False

    return True

# check the public key is pkcs1 or pkcs8
def checkPublicKeyFormat(pubkeypem):
    
    logger.info("Enter function checkPublicKeyFormat")

    pubkeyFormat = ""

    pkcs8_ma = _markers("PUBLIC KEY")
    pkcs1_ma = _markers("RSA PUBLIC KEY") # pkcs1 with RSA more than pkcs8

    if not is_bytes(pubkeypem):
        pubkeypem = pubkeypem.encode('ascii')

    for line in pubkeypem.splitlines():
        line = line.strip()
        
        if (line == pkcs1_ma):
            
            return "pkcs1"
        elif (line == pkcs8_ma):
            return "pkcs8"
        
        else:
            return pubkeyFormat

#this refer the code of python rsa module pem.py
def _markers(pem_marker):
    """
    Returns the start and end PEM markers
    """

    if is_bytes(pem_marker):
        pem_marker = pem_marker.decode('utf-8')

    return (b('-----BEGIN %s-----' % pem_marker))

#if __name__=='__main__':


from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64
from authapp.challenge import getChallengeNumByUserName 
from authapp import models
from authapp.rsaKey import checkPublicKeyFormat
import rsa
import logging

logger= logging.getLogger("django")

#class response:
def responseVerify(usertemp,signtemp):
    logger.info("Enter function responseVerify,user=%s",usertemp)
    #print "Start response Verify!"
    is_verify = False
    try:
        #print rsaSign
        pubkey_dict= models.Publickey.objects.filter(user=usertemp)
        #with open('master-public.pem','r') as f:
           # pubkey_pem=f.read()
        #print pubkey_dict[0].key
        pubkey_pem = base64.b64decode(pubkey_dict[0].key)

        challenge = getChallengeNumByUserName(usertemp)
        if "65536"== challenge:
            logger.errer("the challenge number is 65536,out of the range")
            return False

        signtemp_r=signtemp.replace(" ","+")
        #print signtemp_r
        signature = base64.b64decode(signtemp_r)

        format_pem =  checkPublicKeyFormat(pubkey_pem)
        logger.info("user 's public key is format %s",usertemp,format_pem)
        if ("pkcs1"==format_pem):
            
            publickey = rsa.PublicKey.load_pkcs1(pubkey_pem)

            if rsa.verify(challenge.encode('utf-8'),signature,publickey):
                return True
            else:
                return False 
        elif("pkcs8"==format_pem):
 
            rsakey = RSA.importKey(pubkey_pem)
            verifier = Signature_pkcs1_v1_5.new(rsakey)
            digest = SHA.new()
        
            digest.update(challenge)
            #print digest.hexdigest()
        
            if verifier.verify(digest,signature):
                return True
            return False
    except Exception,e:
        logger.error(e)
        return False

def responseVerifyHMAC(usertemp,hmacCode):
    return True

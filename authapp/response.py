from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64
from authapp.challenge import getChallengeNumByUserName 
from authapp import models

#class response:
def responseVerify(usertemp,signtemp):
    """
    >>> (pubkey, privkey) = rsa.newkeys(512)
    >>> message = 'Go left at the blue tree'
    >>> signature = rsa.sign(message, privkey, 'SHA-1')
    """
    print "Start response Verify!"
    is_verify = False
    try:
        #print rsaSign
        pubkey_dict= models.Publickey.objects.get(user=usertemp)
        #with open('master-public.pem','r') as f:
           # pubkey_pem=f.read()
        pubkey_pem = base64.b64decode(pubkey_dict.key)
        #print usertemp
        print pubkey_pem
        rsakey = RSA.importKey(pubkey_pem)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        challenge = getChallengeNumByUserName(usertemp)
        #print "challenge="+challenge
        if "65536"== challenge:
            print "the challenge number is 65536, out of the range"
            return 
        
        digest.update(challenge)
        print digest.hexdigest()
        signtemp_r=signtemp.replace(" ","+")
        print signtemp_r
        signature = base64.b64decode(signtemp_r)

        print signature
        is_verify=verifier.verify(digest,signature)
        #print is_verify
    except Exception as err:
        print(err)
    print "return from responseVefiry"
    #return is_verify
    if (True == is_verify):
        return True
    elif (False == is_verify):
        return False

def responseVerifyHMAC(usertemp,hmacCode):
    return True

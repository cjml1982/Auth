import hmac
import hashlib
import base64

secreteKey = "!QAZ@WSX#EDC$RFV"

def getHMAC(message):
    h=hmac.new(secreteKey, msg=message, digestmod=hashlib.sha1).digest()
    hmac_b64 = base64.b64encode(h)

    return hmac_b64

def verifyHMAC(digest_b64,message):
    hmac_verify= hmac.new(secreteKey, msg=message, digestmod=hashlib.sha1).digest()

    digest= base64.b64decode(digest_b64)

    return hmac.compare_digest(digest, hmac_verify)


import hmac
import hashlib
import base64

secreteKey = "!QAZ@WSX#EDC$RFV"

message="yilian3333"

h=hmac.new(secreteKey, msg=message, digestmod=hashlib.sha1).digest()
hmac_b64 = base64.b64encode(h)
print hmac_b64

hmac_verify= hmac.new(secreteKey, msg=message, digestmod=hashlib.sha1).digest()
digest= base64.b64decode(hmac_b64)

print hmac.compare_digest(digest, hmac_verify)

#if (digest == hmac_verify):
#    print True
#else:
#    print False

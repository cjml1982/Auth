
from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign
import base64  
      
key = load_privatekey(FILETYPE_PEM, open("master-private.pem").read())  
content = "46060"      
d =  sign(key, content, 'sha1')    
print d
b = base64.b64encode(d)   
print b  

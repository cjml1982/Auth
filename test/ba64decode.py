import base64


with open('sign.txt','r') as f:
    sign=f.read()

sign_ba64 = base64.b64encode(sign)

print sign_ba64

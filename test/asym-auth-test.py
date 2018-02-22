import urllib
import json
import urllib2
import httplib 
 
#url
post_url = "http://127.0.0.1:8000/asym-auth/request/"
 
#postData  = {'a':'aaa','b':'bbb','c':'ccc','d':'ddd'}
postData  ={'user':'yilian111'}
#json serialization
datadump = json.dumps(postData)

#postData_urlencode = urllib.urlencode(datadump)
#headerdata = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}     
headerdata = {"Host":"127.0.0.1"}
#req = urllib2.Request(url=post_url,data=postData_urlencode)
#req = urllib2.Request(url=post_url,data="user:yilian111")

#print req
conn = httplib.HTTPConnection("127.0.0.1",8000)
conn.request(method="POST",url=post_url,body="user=yilian111",headers=headerdata)
 
response =conn.getresponse() 
#response = urllib2.urlopen(req,urllib.urlencode({'sku_info':data}))
#response = urllib2.urlopen(req)
 
#print the response
print response.read()



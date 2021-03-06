#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
#from rest_framwork.views import APIview
from authapp import models
from rest_framework.generics import CreateAPIView
from authapp.challenge import getChallenge,deleteChallenge
from authapp.response import responseVerify
from authapp.authJwt import create_jwt,verify_jwt
from rsaKey import checkKeyFormat
from authapp.authHMAC import getHMAC,verifyHMAC

import logging

#Get an instance of a logger
logger = logging.getLogger('django')

# Create your views here.

def RegisterView(request):

    if request.method !="POST":
        return JsonResponse({"result":"error","message":"null","error":{"code":-103,"info":"Not use POST method"}})
       
    try:
        #if the user already registered
        usertemp= models.Publickey.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    #if user already exist, return error
    if usertemp:
        return JsonResponse({"result":"error","message":"null","error":{"code":-101,"info":"User already registered"}})

#    user_list_obj= models.Publickey.objects.all()
#    return render(request,'t1.html',{'li':user_list_obj})
#    dic ={"user":"asdkjfsd","key":"addfdfsdsdgdsgds"}
#    models.Publickey.objects.create(**dic)
    user= request.POST['user']
    key=request.POST['publickey']

    logger.info("Register user=%s,key=%s",user,key)

    #maybe the publickey base64 code, hase '+' simble,the base64 code '+' would be transfer to a blank space, the blank space should be transfer to '+' again
    key=key.replace(" ","+")

    result = checkKeyFormat(user,key)
    if (True == result):
        try:
            #create the user with publickey
            models.Publickey.objects.create(user=request.POST['user'],key=request.POST['publickey'])
        except Exception,e:
            logger.error(e)

        return JsonResponse({"result":"success","message":{"name":"Register Success"},"error":"null"})
    else:
        return JsonResponse({"result":"error","message":"null","error":{"code":-102,"info":"Public key format error"}})

def RequestView(request):

    if request.method != "POST":
        return JsonResponse({"result":"error","message":"null","error":{"code":-103,"info":"Not use POST method"}})

    try:
        usertemp = models.Publickey.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    #if user exist, return challenge
    if usertemp:
        user= request.POST['user']
        challengeNum =getChallenge(user)
    
        logger.info("authRequest user=%s,challenge=%s",user,challengeNum)
    #if user not exist,reject
    else:
        return JsonResponse({"result":"error","message":"null","error":{"code":-201,"info":"User not exist"}})


    return JsonResponse({"result":"success","message":{"name":"Challenge","random":challengeNum},"error":"null"})


def ResponseView(request):

    if request.method != "POST":
        return JsonResponse({"result":"error","message":"null","error":{"code":-103,"info":"Not use POST method"}})

    try:
        user_dict = models.Publickey.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    #if user not exist
    if not user_dict:
        return JsonResponse({"result":"error","message":"null","error":{"code":-201,"info":"User not exist"}})

    try:
        challenge_dict = models.Challenge.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    if not challenge_dict:
        return JsonResponse({"result":"error","message":"null","error":{"code":-302,"info":"Challenge number not exist"}})

    user= request.POST['user']
    signtemp = request.POST['signature']
    logger.info("response user=%s,sign=%s",user,signtemp)

    verify_result=False    
    verify_result = responseVerify(user,signtemp)
    #print "End of responseVerify"

    #no matter the result of verify it ture or false,the challenge number should be deleted,to avoid the retry attack,the deleteChallenge can be disableed for testing 
    deleteChallenge(user)

    if (True == verify_result): 
        jwt_token=create_jwt(user)
        return JsonResponse({"result":"success","message":{"name":"Return","JWT":jwt_token},"error":"null"})

    else:
        return JsonResponse({"result":"error","message":"null","error":{"code":-301,"info":" Verify the signature fail "}})

def AuthView(request):
    if request.method != 'POST':
        return JsonResponse({"result":"error","message":"null","error":{"code":-103,"info":"Not use POST method"}})

    try:
        user_dict = models.Publickey.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    #if user not exist
    if not user_dict:
        return JsonResponse({"result":"error","message":"null","error":{"code":-201,"info":"User not exist"}})

    usertemp = request.POST['user']
    authjwt= request.POST['Authorization']

    logger.info("auth user=%s, jwt=%s",usertemp,authjwt)
    try:
        result = verify_jwt(usertemp,authjwt)
    except Exception ,e:
        logger.error(e)

    if (True == result):
        return JsonResponse({"result":"success","message":{"name":"Auth Success"},"error":"null"})
    elif (False==result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-401,"info":"JWT verify fail"}})
    elif('expired'==result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-402,"info":"JWT expired"}})
    elif('unAuth'==result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-403,"info":"User has no permissions"}})


#reserved for further function
def UpdateView(request,**kwargs):
    #if 'Authorization' in request.headers:
    functiontemp = kwargs.get('function',None)
    #urlid = kwargs.get('id',None)
    if request.method != 'POST':
        return JsonResponse({"result":"error","message":"null","error":{"code":-103,"info":"Not use POST method"}})

    try:
        user_dict = models.Publickey.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    #if user not exist
    if not user_dict:
        return JsonResponse({"result":"error","message":"null","error":{"code":-201,"info":"User not exist"}})

    usertemp = request.POST['user']
    authjwt= request.POST['Authorization']

    #print authjwt
    try:
        result = verify_jwt(usertemp,authjwt)
    except Exception ,e:
        logger.error(e)

    if (True == result):
        logger.info("JWT vefify success,auth user=%s, jwt=%s",usertemp,authjwt)
    elif (False==result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-401,"info":"JWT verify fail"}})
    elif('expired'==result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-402,"info":"JWT expired"}})
    elif('unAuth'==result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-403,"info":"User has no permissions"}})

    #function process
    if ('updatePublickey'==functiontemp):
        keytemp=request.POST['publickey']
        #replace the blank space to "+"
        keytemp=keytemp.replace(" ","+")

        #check the public key format
        result = checkKeyFormat(usertemp,keytemp)
        if (True == result):
            try:
                #update the user with publickey
                models.Publickey.objects.filter(user=usertemp).update(key=keytemp)
            except Exception,e:
                logger.error(e)

            return JsonResponse({"result":"success","message":{"name":"Publickey update Success"},"error":"null"})
        else:
            return JsonResponse({"result":"error","message":"null","error":{"code":-102,"info":"Public key format error"}})

    elif ('deleteUser'==functiontemp):
        try:
            models.Publickey.objects.filter(user=usertemp).delete()
        except Exception,e:
            logger.error(e)

        return JsonResponse({"result":"success","message":{"name":"Delete User Success"},"error":"null"})


    else:
        return JsonResponse({"result":"error","message":"null","error":{"code":-202,"info":"The update interface not exist"}})


def AdminView(request,**kwargs):

    if request.method !="POST":
        return JsonResponse({"result":"error","message":"null","error":{"code":-103,"info":"Not use POST method"}})

    functiontemp = kwargs.get('function',None)

    try:
        user_dict = models.Publickey.objects.filter(user=request.POST['user'])
    except Exception,e:
        logger.error(e)

    #if user not exist
    if not user_dict:
        return JsonResponse({"result":"error","message":"null","error":{"code":-201,"info":"User not exist"}})

    usertemp = request.POST['user']
    authHMAC= request.POST['Authorization']

    result = verifyHMAC(authHMAC,usertemp)

    if(False == result):
        return JsonResponse({"result":"error","message":"null","error":{"code":-104,"info":"The admin auth fail"}})

    #function process
    if ('deleteUser'==functiontemp):
        try:
            models.Publickey.objects.filter(user=usertemp).delete()
        except Exception,e:
            logger.error(e)

        return JsonResponse({"result":"success","message":{"name":"Delete User Success"},"error":"null"})

    else:
        return JsonResponse({"result":"error","message":"null","error":{"code":-202,"info":"The update interface not exist"}})


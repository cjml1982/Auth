# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
#from rest_framwork.views import APIview
from django.shortcuts import render
from authapp import models
from rest_framework.generics import CreateAPIView
from authapp.challenge import getChallenge
from authapp.response import responseVerify
from authapp.authJwt import create_jwt,verify_jwt

# Create your views here.

def RegisterView(request):

    if request.method =="POST":
        models.Publickey.objects.create(user=request.POST['user'],key=request.POST['publickey'])
#    user_list_obj= models.Publickey.objects.all()
#    return render(request,'t1.html',{'li':user_list_obj})
#    dic ={"user":"asdkjfsd","key":"addfdfsdsdgdsgds"}
#    models.Publickey.objects.create(**dic)

    return JsonResponse({"message":"Register Success!"})

def RequestView(request):
    if request.method == "POST":
        user= request.POST['user']
    challengeNum =getChallenge(user)

    return JsonResponse({"message":"Challenge","random":challengeNum})

def ResponseView(request):
    #print "start Response View"
    if request.method == "POST":
        usertemp= request.POST['user']
        print "usertemp "+ usertemp
        signtemp = request.POST['signature']
        print "sign "+ signtemp
        #verify_result= reponseVerify(usertemp,signtemp)
    else:
        return JsonResponse({"message":"Error"})

    verify_result=False
    #try:    
    verify_result= responseVerify(usertemp,signtemp)
    print verify_result
    #except Exception as err:
       # print(err)

    if (True == verify_result): 

        jwt_token=create_jwt(usertemp)
        if None == jwt_token:
            return JsonResponse({"message":"Return","Reason":"Token fail"})
        #jwt_token="dsfasdads"
        return JsonResponse({"message":"Return","JWT":jwt_token})
    elif (False==Verify_result):
        return JsonResponse({"message":"Return","Reason":"Verify Failure!"})

    return JsonResponse({"message":"Return","Reason":"Error!"})


def AuthView(request,**kwargs):
    #if 'Authorization' in request.headers:
    function = kwargs.get('function',None)
    urlid = kwargs.get('id',None)
    print function, urlid
    if request.method == 'POST':
        usertemp = request.POST['user']
        authjwt= request.POST['Authorization']
    else:
        return JsonResponse({"message":"Error"})
    
    print authjwt
    try:
        result = verify_jwt(usertemp,authjwt)
    except Exception ,e:
        print e

    return JsonResponse({"message":"auth true"}) 

import rsa
import random
from authapp import models
import string

challengeDict ={}

def getChallenge(usertemp):
    challengeNum = str(random.randint(0,65535))
    try:
        models.Challenge.objects.create(user=usertemp,challenge=challengeNum)
    except Exception as err:
        print(err)
    #if Usertemp in challengeDict.keys():
        #challengeDict[Usertemp]=[challengeNum]
    #else:
        #challengeDict[Usertemp]=[challengeNum]
    #print challengeDict
    return challengeNum

def getChallengeNumByUserName(usertemp):
    challenge = str(65536)
    #if Usertemp in challengeDict.keys():
        #numlist = challengeDict.get(Usertemp)
        #print numlist
    challenge_dict= models.Challenge.objects.get(user=usertemp)
    challenge = challenge_dict.challenge
    return challenge

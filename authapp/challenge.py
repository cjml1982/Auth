import rsa
import random
from authapp import models
import string
import logging

logger= logging.getLogger("django")

def getChallenge(usertemp):
    logger.info("Enter function getChallenge,user=%s",usertemp)
    try:
        challengetemp = models.Challenge.objects.filter(user=usertemp)
    except Exception,e:
        logger.error(e)

    if challengetemp:
        logger.error("challenge number exist for user %s",usertemp)
        return challengetemp[0].challenge

    challengeNum = str(random.randint(0,65535))
    try:
        models.Challenge.objects.create(user=usertemp,challenge=challengeNum)
    except Exception, e:
        logger.error(e)
    
    return challengeNum

def deleteChallenge(usertemp):
    logger.info("Enter function deleteChallenge,user=%s",usertemp)
    try:
        models.Challenges.objects.filter(user=usertemp).delete()
    except Exception,e:
        logger.error(e)

    return True

def getChallengeNumByUserName(usertemp):
    logger.info("Enter function getChallengeNumByUserName, user= %s",usertemp)

    try:
        challenge_dict= models.Challenge.objects.filter(user=usertemp)
        challenge = challenge_dict[0].challenge
    except Exception,e:
        logger.error(e)
        return "65536"        

    return challenge

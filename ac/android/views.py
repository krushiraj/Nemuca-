from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
import datetime
from django.core import serializers
from core.models import Details
from core.models import RegistrationsAndParticipations
from core.models import Event
from core.models import Profile
from django.db.models import F
from itertools import chain
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
#-----------------------------------------------------------------------------------------------------------------------------------------
#EVENT-IDS


#AWD  -  A WALK IN THE DARK
#AER  -  AEROPLANE CHESS
#ALP    -  ALPATCHINO
#ANW  -  ANWEHSA
#BYC  -  BEYCODE
#CHL - CHALLENGICA
#CRC  - CRIMINAL CASE
#CRP  -  CRYPTOTHON
#DXT  - DEXTRA
#KOT  -  KNOCK OFF TOURNAMENT
#TTX  - TECHTRIX

#-----------------------------------------------------------------------------------------------------------------------------------------
#Results Fetch

#Use this function to get end results, Need to modify based upon various filters
@csrf_exempt
def showDetails(request):
    if request.method == 'POST':
        queryset = Details.objects.filter(eId = request.POST.get('eId'))
        json_data = serializers.serialize('json',queryset)
        return HttpResponse(json_data, content_type = "application/json")


@csrf_exempt
def showRegistrationsAndParticipations(request):
    queryset = RegistrationsAndParticipations.objects.all().order_by('pk')
    json_data = serializers.serialize('json',queryset)
    return HttpResponse(json_data, content_type = "application/json")

def showEvent(request):
    queryset = Event.objects.all.order_by('pk')
    json_data = serializers.serialize('json',queryset)
    return HttpResponse(json_data, content_type = "application/json")

#----------------------------------------------------------------------------------------------------------------------
# Event App

#Takes Existing Gid and adds Players
# URL @ events/addplayer
@csrf_exempt
def appendPlayers(request):
    message = 'Err '
    if request.method == 'POST':
        qID = request.POST.get('qId').split(',')
        gID = request.POST.get('gId')
        # Got data
        queryset = Details.objects.filter(gId = gID)
        #If this game even exists
        if queryset:
            #Check for list of qID's are valid or not
            for s in qID:
                if not validateGame(queryset.eID,s):
                    user = Profile.objects.get(qId = qID)
                    json_data = sorted(chain(user, queryset))
                    #json_data = user | obj
                    json_data = serializers.serialize('json',user)
                    return HttpResponse(user, content_type = "application/json")
                    message.append(s)
                    #return HttpResponse(message, content_type = "text/plain")

            # Append qID ( list ) to queryset
                else:
                    queryset.QId.append(s)

            queryset.status = 'Running'
            queryset.save()
            message = 'Success'
            #Anthe I guess
    else:
        message = 'Invalid Request'

    return HttpResponse(message, content_type = "text/plain")



#Ends the game adding score and updating participated
# URL events/endgame
@csrf_exempt
def endGame(request):
    message = 'Err'
    if request.method == 'POST':
        GID =  request.POST.get('gId')
        score = request.POST.get('Total')
        #fetch the row with give gId
        queryset = Details.objects.get(gId = GID)
        #update status and score
        #queryset.update(status = 'Played',Total = score)
        queryset.status_choice = 'Played'
        queryset.Total = score
        queryset.save()
        #append to participated list
        EID = queryset.eId.eId
        lists = queryset.QId
        for q in lists:
            profile = Profile.objects.get(QId= q)
            kp = profile.pk
            c = RegistrationsAndParticipations.objects.get(QId = kp)
            print("EID : ",EID)
            print("Participated : ",c.participated)
            c.participated.append(EID)
            c.save()
            print("updated : ",c.participated)

        #queryset.save()
        message = 'Done'
        pass
    else:
        message = 'Invalid Request'
        pass
    return HttpResponse(message, content_type = "text/plain")

#Generates unique GID which doesn't occur in the data base
@csrf_exempt
def generateGID(eID):
    game = Event.objects.get(eId = eID)
    game.eCount = game.eCount+1
    game.save()
    return "%s%s" %(eID,game.eCount)


#Creates a New Game with a single Qid
# URL events/newgame
@csrf_exempt
def newGame(request):
    message = 'Err'
    if request.method == 'POST':
        eId = request.POST.get('eId')
        qId = request.POST.get('qId')
        print("Hii")
        #Collected Required Data
        #Checking for valid QID for this game
        if validateGame(eId,qId):
            #Generating New Game ID
            print("Validate Worked fine")
            #detail = Details.objects.get(gId = 'TTX2')
            #print(detail.eId)
            gId = generateGID(eId)
            #Creating New Row
            event = Event.objects.get(eId=eId)
            eventId = event.eId
        
            obj = Details( eId = Event.objects.get(eId=eId), QId = [qId,], Total = 0, gId = gId, status_choice = 'Waiting' )
            obj.save()
            #commiting the row
            message = 'Success'
            userP = Profile.objects.get(QId = qId)
           
            json1 = serializers.serialize('json',[obj,userP])
            #json_data = user | obj
            return HttpResponse(json1, content_type = "application/json")
        else:
            message = 'User cannot play this game'

    else:
        message = 'Not a Valid Request'

    return HttpResponse(message, content_type = "text/plain")




#Authenticates user to the game
#Checks if the user is playing for the first time or not! ^.^
@csrf_exempt
def validateGame(eId,qId):
    print('abc')
    flag = False
    #Get the row in this model for the corresponding user
    profile = Profile.objects.get(QId= qId)
    kp = profile.pk
    check = RegistrationsAndParticipations.objects.get(QId = kp)
    #Check if user elgible ie. paid and not participated and registered
    if eId in check.paid and eId in check.registered:
        if eId not in check.participated:
            flag = True

    return flag

#------------------------------------------------------------------------------------------------------------------------------------------------
#Registrations

# URL register/fetch
@csrf_exempt
def getUserEvent(request):
    message = 'Err'
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(QId= request.POST.get('qId'))
        except ObjectDoesNotExist:
            return HttpResponse("QR Code is not valid",content_type="text/plain")
        kp = profile.pk
        query = RegistrationsAndParticipations.objects.filter(QId = kp)
        if not query:
            return HttpResponse("Nope",content_type="text/plain")
        #Need to remove participated column

        json_data = serializers.serialize('json',query)
        return HttpResponse(json_data,content_type = "application/json")
    else:
        return HttpResponse(message , content_type = "text/plain")

#Replace
# URL register/push
@csrf_exempt
def modifyRegistrationsAndParticipations(request):
    message = 'Err'
    if request.method == 'POST':
        #profile = Profile.objects.get(QId= request.POST.get('qId'))
        #kp = profile.pk
        
        #QId can directly be fetched here.
        queryset = RegistrationsAndParticipations.objects.get( QId = request.POST.get('QId'))
        #Fetch request Data
        registered = request.POST.get('registered')
        paid = request.POST.get('paid')
        #look and replace the fields
        #Removing Current Data
        
        queryset.paid = paid.split(',')
        queryset.registered = registered.split(',')
        
        queryset.save()

        message = 'Success'

    else:
        message ='Invalid Request'

    return HttpResponse(message, content_type = "text/plain")




#---------------------------------------------------------------------------------------------------------------------------------------------------
#This is your code , appending the written code into templates can help us sort it out
# def add_participant(request):
#     if request.method == 'POST':
#         queryset = RegistrationsAndParticipations.objects.all().get(Qid = request.POST.get('QId'))
#         if queryset:
#             if request.POST.get('eId') in queryset.paid:
#                 if request.POST.get('eId') in queryset.participated:
#                     #return render(request,'',{'error_message' = error_message})
#                 else:
#                     gameId = get_random_string(length = 5)
#                     dup_game = Details.objects.get(gId = get_random_string(length = 5))
#                     if dup_game:
#                         return render(request,'',{'error_message' = error_message})
#                     else:
#                         nEvent = Details(status = "Running", eId = request.POST.get('eId'), gId = gameId, QId = request.POST.get('QId'), Total = 0)
#                         nEvent.save()
#                         json_data = serializers.serialize('json',nEvent)
#                         return HttpResponse(json_data, content_type = "application/json")
#             else:
#                 return render(request,'',{'error_message' = error_message})
#     else:
#         return render(request,'',{'error_message' = error_message})
#         # json_data = serializers.serialize('json', queryset)
#         # return HttpResponse(json_data, content_type = "application/json")

# #This will be final request, where
# def add_scores(request):
#     if request.method = 'POST':
#         queryset1 = Details.objects.filter(gId = request.POST.get('gId')).update(status = "Played", Total = request.POST.get('Total'))
#         queryset2 = RegistrationsAndParticipations.objects.filter(QId = queryset1.QId)
#         for obj in queryset2:
#             obj.participated.append(queryset1.eId)
#             obj.save()
#         json_data = serializers.serialize('json', queryset2)
#         return HttpResponse(json_data, content_type = "application/json")
























# def register(request):
#     if request.method = 'POST':
#         queryset = Profile.objects.get(QId = request.POST.get('QId'))
#         if queryset:
#             queryset1 = RegistrationsAndParticipations.objects.get(QId = queryset.QId)
#             Event = request.POST.get('eId')
#             queryset1.paid.append(Event)
#             json_data = serializers.serialize('json', queryset1)
#             return HttpResponse(json_data, content_type = "application/json")

#         # else:

#         # 	Profile.objects.create()
#         # 	q1 = Profile.objects.get(QId)
#         # 	Event = request.POST.eId
#         # 	e1 = RegistrationsAndParticipations.objects.get(QId = q1.QId)
#         # 	e1.paid.append(Event)

#         else:
#             #messages.error(request, 'ERR
#             return render(request,'',{'error_message' = error_message})a

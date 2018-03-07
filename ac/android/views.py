from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
import datetime
from django.core import serializers
from .models import EventDetails
from .models import RegistrationsAndParticipations

from django.db.models import F

from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt



#-----------------------------------------------------------------------------------------------------------------------------------------
#Results Fetch

#Use this function to get end results, Need to modify based upon various filters
def showEventdetails(request):
    if request.method == 'POST':
        queryset = EventDetails.objects.filter(eId = request.POST.get('eId'))
        return render(request,'',{'queryset':queryset})



#----------------------------------------------------------------------------------------------------------------------
# Events App

#Takes Existing Gid and adds Players
def appendPlayers(request):
    message = 'Err '
    if request.method == 'POST':
        qID = request.post.get('qId').split(',')
        gID = request.post.get('gId')
        # Got data
        queryset = EventDetails.objects.filter(gId = gID)
        #If this game even exists
        if queryset:
            #Check for list of qID's are valid or not
            for s in qID:
                if not validate(queryset.eID,s):
                    message.append(s)
                    return HttpResponse(message, content_type = "text/plain")
            
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
def endGame(request):
    message = 'Err'
    if request.method == 'POST':
        GID =  request.POST.get('gId')
        score = request.POST.get('Total')
        queryset = EventDetails.objects.get(gId = GID)
        
        pass
    else:
        pass
    return HttpResponse(message, content_type = "text/plain")

#Generates unique GID which doesn't occur in the data base
def generateGID(eID):
    game = Events.objects.get(eId = eID)
    game.eCount = F('eCount')+1
    game.save()
    return "%s%s" %(eID,game.eCount)


#Creates a New Game with a single Qid
def newGame(request):
    message = 'Err'
    if request.method == 'POST':
        eID = request.post.get('eId')
        qID = request.post.get('qId')
        #Collected Required Data
        #Checking for valid QID for this game
        if validateGame(qId,eId):
            #Generating New Game ID
            gID = generateGID(eID)
            #Creating New Row
            obj = EventDetails( eId = eID, qId = qID, Total = 0, gId = gID, status = 'Waiting' )
            obj.save()
            #commiting the row 
            message = 'Success'
        else:
            message = 'Not Applicable'
    else:
        message = 'Not a Valid Request'

    return HttpResponse(message, content_type = "text/plain")
        
    
    

#Authenticates user to the game
#Checks if the user is playing for the first time or not! ^.^
def validateGame(eId,qID):
    flag = False
    #Get the row in this model for the corresponding user
    check = RegistrationsAndParticipations.objects.all().get(qId = qID)

    #Check if user elgible ie. paid and not participated and registered
    if eId in check.paid and check.registered:
        if eID not in check.participated:
            flag = True

    return flag

#------------------------------------------------------------------------------------------------------------------------------------------------
#Registrations

def getUserEvents(request):
    message = 'Err'
    if request.method == 'POST':
        # Fetch Registrations and participations for paid registered and participated
        query = RegistrationsAndParticipations.objects.filter( qId = request.post.get('qId'))
        #Need to remove participated column
        json_data = serializers.serialize('json',query)
        return HttpResponse(json_data,content_type = "json/application")
    else:
        return HttpResponse(message , content_type = "text/plain")

#Replace 
def modifyRegistrationsAndParticipations(request):
    message = 'Err'
    if request.method == 'POST':
        queryset = RegistrationsAndParticipations.objects.filter( qId = request.post.get('qId'))
        #Fetch request Data
        #pariticapted = request.post.get('participated')
        registered = request.post.get('registered')
        paid = request.post.get('paid')
        #look and replace the fields
        #Removing Current Data
        queryset.paid = []
        queryset.registered = []
        #Adding new data
        queryset.paid = paid
        queryset.registered = registered
               
        
        for s in paid:
            queryset.paid.append(s)  
        for s in registered:
            queryset.registered.append(s)
        
        #all operations done
        queryset.save()

        message = 'Success' 

    else:
        message ='Invalid Request'

    return HttpResponse(message, content_type = "text/plain")
        



#---------------------------------------------------------------------------------------------------------------------------------------------------
#This is your code , appending the written code into templates can help us sort it out
def add_participant(request):
    if request.method == 'POST':
        queryset = RegistrationsAndParticipations.objects.all().get(Qid = request.POST.get('QId'))
        if queryset:
            if request.POST.get('eId') in queryset.paid:
                if request.POST.get('eId') in queryset.participated:
                    #return render(request,'',{'error_message' = error_message})
                else:
                    gameId = get_random_string(length = 5)
                    dup_game = EventDetails.objects.get(gId = get_random_string(length = 5))
                    if dup_game:
                        return render(request,'',{'error_message' = error_message})
                    else:
                        nEvent = EventDetails(status = "Running", eId = request.POST.get('eId'), gId = gameId, QId = request.POST.get('QId'), Total = 0)
                        nEvent.save()
                        json_data = serializers.serialize('json',nEvent)
                        return HttpResponse(json_data, content_type = "application/json")
            else:
                return render(request,'',{'error_message' = error_message})
    else:
        return render(request,'',{'error_message' = error_message})
        # json_data = serializers.serialize('json', queryset)
        # return HttpResponse(json_data, content_type = "application/json")

#This will be final request, where 
def add_scores(request):
    if request.method = 'POST':
        queryset1 = EventDetails.objects.filter(gId = request.POST.get('gId')).update(status = "Played", Total = request.POST.get('Total'))
        queryset2 = RegistrationsAndParticipations.objects.filter(QId = queryset1.QId)
        for obj in queryset2:
            obj.participated.append(queryset1.eId)
            obj.save()
        json_data = serializers.serialize('json', queryset2)
        return HttpResponse(json_data, content_type = "application/json")
























# def register(request):
#     if request.method = 'POST':
#         queryset = Profile.objects.get(QId = request.POST.get('QId'))
#         if queryset:
#             queryset1 = RegistrationsAndParticipations.objects.get(QId = queryset.QId)
#             Events = request.POST.get('eId')
#             queryset1.paid.append(Events)
#             json_data = serializers.serialize('json', queryset1)
#             return HttpResponse(json_data, content_type = "application/json")
        
#         # else:
        
#         # 	Profile.objects.create()
#         # 	q1 = Profile.objects.get(QId)
#         # 	events = request.POST.eId
#         # 	e1 = RegistrationsAndParticipations.objects.get(QId = q1.QId)
#         # 	e1.paid.append(events)
        
#         else:
#             #messages.error(request, 'ERR
#             return render(request,'',{'error_message' = error_message})a




 

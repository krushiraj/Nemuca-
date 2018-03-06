from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
import datetime
from django.core import serializers
from .models import EventDetails
from .models import RegistrationsAndParticipations



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
    message = 'Err'
    if request.method == 'POST':
        qID = request.post.get('qId')
        gID = request.post.get('gId')

        queryset = RegistrationsAndParticipations.objects.all.filter(gId = gID)
        # append this eId to the query and submit it. Idk how to append

    pass

#Ends the game adding score and updating participated
def endGame(request):
    pass

#Generates unique GID which doesn't occur in the data base
def generateGID():
    #Emo lol em chestunam ida naku telidu, If its random write a checking function to check for duplicates
    pass

#Creates a New Game with a single Qid
def newGame(request):
    message = 'Err'
    if request.method == 'POST':
        eID = request.post.get('eId')
        qID = request.post.get('qId')
       
        if validateGame(qId,eId):
            gID = generateGID()
            status = 'waiting'
            obj = EventDetails( eId = eID, qId = qID, Total = 0, gId = gID, status = 'Waiting' )
            obj.save()

        else:
            message = 'Not Applicable'
    else:
        message = 'Not a Valid Request'

    return HttpResponse(message, content_type = "text/plain")
        
    
    

#Authenticates user to the game
#Checks if the user is playing for the first time or not! ^.^
def validateGame(eId,qId):
    flag = False
    check = RegistrationsAndParticipations.objects.all().get(qId = qId)
    if eId in check.paid and check.participated:
        flag = True
    return flag

#------------------------------------------------------------------------------------------------------------------------------------------------
#Registrations



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




 

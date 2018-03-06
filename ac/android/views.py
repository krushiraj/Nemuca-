# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
# from core.models import Events, EventDetails
# from .serializers import EventsSerializer

# class EventsView(ListAPIView):
#     queryset = EventDetails.objects.all().order_by('-eventname')
#     serializer_class = EventsSerializer

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
def appendGame(request):
    pass

#Ends the game adding score and updating participated
def endGame(request):
    pass

#Generates unique GID which doesn't occur in the data base
def generateGID():
    pass

#Creates a New Game with a single Qid
def newGame(request):
    pass

#Authenticates user to the game
#Checks if the user is playing for the first time or not! ^.^
def validateGame():
    pass

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




 

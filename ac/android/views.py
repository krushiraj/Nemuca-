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


def showEventdetails(request):
    if request.method == 'POST':
        queryset = EventDetails.objects.filter(eId = request.POST.get('eId'))
        return render(request,'',{'queryset':queryset})

def add_participant(request):
    if request.method == 'POST':
        queryset = RegistrationsAndParticipations.objects.all().get(Qid = request.POST.QId)
        if queryset:
            if request.POST.eId in queryset.paid:
                if request.POST.eId in queryset.participated:
                    return render(request,'',{'error_message' = error_message})
                else:
                    nEvent = EventDetails(status = "Running", eId = request.POST.get('eId'), gId, QId = request.POST.get('QId'), Total = 0)
                    nEvent.save()
                    json_data = serializers.serialize('json',nEvent)
                    return HttpResponse(json_data, content_type = "application/json")
            else:
                return render(request,'',{'error_message' = error_message})
    else:
        return render(request,'',{'error_message' = error_message})
        # json_data = serializers.serialize('json', queryset)
        # return HttpResponse(json_data, content_type = "application/json")

def add_scores(request):
    if request.method = 'POST':
        queryset1 = EventDetails.objects.filter(gId = request.POST.gId).update(status = "Played", Total = request.POST.Total)
        queryset2 = RegistrationsAndParticipations.objects.filter(QId = queryset1.QId)
        for obj in queryset2:
            obj.participated.append(queryset1.eId)
            obj.save()
        json_data = serializers.serialize('json', queryset2)
        return HttpResponse(json_data, content_type = "application/json")

def register(request):
    if request.method = 'POST':
        queryset = Profile.objects.get(QId = request.POST.QId)
        if queryset:
            queryset1 = RegistrationsAndParticipations.objects.get(QId = queryset.QId)
            Events = request.POST.eId
            queryset1.paid.append(Events)
            json_data = serializers.serialize('json', queryset1)
            return HttpResponse(json_data, content_type = "application/json")
        
        # else:
        
        # 	Profile.objects.create()
        # 	q1 = Profile.objects.get(QId)
        # 	events = request.POST.eId
        # 	e1 = RegistrationsAndParticipations.objects.get(QId = q1.QId)
        # 	e1.paid.append(events)
        
        else:
            #messages.error(request, 'ERR
            return render(request,'',{'error_message' = error_message})a




 

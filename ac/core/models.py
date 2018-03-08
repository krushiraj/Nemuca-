from django.db.models import Model
from django.db import models
from django.contrib.postgres.fields import ArrayField


# START

class Event(Model):

		eId = models.CharField(max_length=3,default = "NULL")
		eName = models.CharField(max_length=50)
		eCount = models.IntegerField(default = 0)

		def __str__(self):
			return self.eName
                
        #def get_gameId(self):
            #return "%s %s" %(self.eId,self.eCount)

class Details(Model):

		Waiting = 'W'
		Running = 'R'
		Played ='P'

		STATUS_CHOICES=((Running,'Running'),(Played,'Played'),(Waiting,'Waiting'))

		status_choice = models.CharField(max_length=8, choices=STATUS_CHOICES)
		eId=models.OneToOneField('Event', max_length=5,on_delete='CASCADE')
		gId=models.CharField(max_length=5)
		QId=ArrayField(models.CharField(max_length = 5))
		Total=models.IntegerField(default = 0)
		date_time=models.DateTimeField('Date Published', auto_now=True)


class RegistrationsAndParticipations(Model):

		QId = models.OneToOneField('Profile', max_length=5, on_delete='CASCADE')
		paid = ArrayField(models.CharField(max_length=5))
		registered = ArrayField(models.CharField(max_length=5))
		participated = ArrayField(models.CharField(max_length=5))


class Hits(Model):

		count = models.IntegerField()


class Media(Model):


		mediaType = models.CharField(max_length=20)
		link = models.TextField()

class Profile(Model):
    QId = models.CharField(max_length=5)
"""
class User(Model):
	email = models.EmailField(max_length=70,blank=True)
	username = models.CharField(max_length=25,blank=True)
	password1 = models.CharField(max_length=25,blank=True)
	password2 = models.CharField(max_length=25,blank=True)
	is_active = models.BooleanField(default = False)
"""
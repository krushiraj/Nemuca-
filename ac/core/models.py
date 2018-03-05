from django.db.models import Model
from django.db import models
from django.contrib.postgres.fields import ArrayField


# START

class Events(Model):

		eventid = models.CharField(max_length=5)
		eventname = models.CharField(max_length=50)

		def __str__(self):
			return self.eventname

class EventDetails(Model):

		Running = 'R'
		Played ='P'

		STATUS_CHOICES=((Running,'Running'),(Played,'Played'))

		status_choice = models.CharField(max_length=8, choices=STATUS_CHOICES)
		eId=models.OneToOneField('Events', max_length=5,on_delete='CASCADE')
		gId=models.CharField(max_length=5)
		QId=models.OneToOneField('Profile', max_length=5,on_delete='CASCADE')
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
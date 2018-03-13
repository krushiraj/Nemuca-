from django.db.models import Model
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# START

class Event(Model):

		eId = models.CharField(max_length=3,default = "NULL")
		eName = models.CharField(max_length=50)
		eCount = models.IntegerField(default = 0)

# 		def __str__(self):
# 			return self.eId
                
        #def get_gameId(self):
            #return "%s %s" %(self.eId,self.eCount)

class Details(Model):

		Waiting = 'W'
		Running = 'R'
		Played ='P'

		STATUS_CHOICES=((Running,'Running'),(Played,'Played'),(Waiting,'Waiting'))

		status_choice = models.CharField(max_length=8, choices=STATUS_CHOICES)
		eId=models.ForeignKey('Event', max_length=5,on_delete='CASCADE')
		gId=models.CharField(max_length=7)
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
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    
    YEAR_CHOICES=((I,'I'),(II,'II'),(III,'III'),(IV,'IV'))
    
    IT = 'IT'
    EEE = 'EEE'
    ECE = 'ECE'
    CIVIL = 'CIVIL'
    CSE = 'CSE'
    MECH = 'MECH'
    CHEMICAL = 'CHEMICAL'
    EIE = 'EIE'
    TEXTILE = 'TEXTILE'
    
    BRANCH_CHOICES=((IT,'Information Technology'),(EEE,'Electronics and Electrical Engineering'),(ECE,'Electronics and Communication Engineering'),(CIVIL,'Civil'),(CSE,'Computer Sciece'),(MECH,'Mechanical'),(CHEMICAL,'Chemical'),(EIE,'Electronics and Instrumentation Engineering'),(TEXTILE,'Textile'))
    
    VCE = 'VCE'
    GRIET = 'GRIET'
    CBIT = 'CBIT'
    VNR = 'VNR'
    MGIT = 'MGIT'
    
    COLLEGE_CHOICES=((VCE,'Vasavi College of Engineering'),(GRIET,'Gokaraju Rangaraju'),(CBIT,'Chaitanya Bharathi Institute'),(VNR,'Vignan Jyothi'),(MGIT,'Mahatma Gandhi Institute'))
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null= True)
    email = models.CharField(max_length = 40, default = "example@abc.com")
    QId = models.CharField(max_length=5, default = "NOQID")
    roll = models.CharField(max_length= 20, default = "1602-70-700-777")
    Year = models.CharField(max_length = 2, choices = YEAR_CHOICES, default = "I")
    Branch = models.CharField(max_length=50,choices = BRANCH_CHOICES, default = "IT")
    College = models.CharField(max_length=50,choices = COLLEGE_CHOICES, default = "VCE")
    Phone_number =models.CharField(max_length=10, default ="NoNumber")

# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Profile(user=user)
#     profile.save()


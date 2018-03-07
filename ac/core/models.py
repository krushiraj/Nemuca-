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
    
    QId = models.CharField(max_length=5)
    Name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    Year = models.CharField(max_length = 2, choices = YEAR_CHOICES)
    Branch = models.CharField(max_length=50,choices = BRANCH_CHOICES)
    College = models.CharField(max_length=50,choices = COLLEGE_CHOICES)
    Phone_number =models.CharField(max_length=10)


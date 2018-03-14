from django.shortcuts import render, redirect
import os
import pyqrcode as pyq
import png
from django.http import Http404
from .models import Profile,Details,RegistrationsAndParticipations
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
# from PIl import Image

#Create your views here.
#@login_required(redirect_field_name='loginpage')
def events(request):
	return render(request, 'eventre.html',{})

#@login_required(redirect_field_name='loginpage')
def gallery(request):
	return render(request, 'gallery.html',{})

#@login_required(redirect_field_name='loginpage')
def index(request):
	return render(request, 'index.html',{})

#@login_required(redirect_field_name='loginpage')
def home(request):
	return render(request,'home.html',{})

#@login_required(redirect_field_name='loginpage')
def maps(request):
	return render(request,'map.html',{})

#@login_required(redirect_field_name='loginpage')
def mapsd(request):
	return render(request,'3dmap.html',{})

def loginpage(request):
	return render(request,'login.html',{})

def loginvalidate(request):
	if request.method == 'POST':
		user = Profile.objects.get(email = request.POST.get('user'))
		if user.password == request.POST.get('password'):
			qrcode = user.QId
			image_data = open(qrcode+'.png', "rb").read()
			return HttpResponse(image_data,content_type='image/png')
		else:
			error_message = request.POST.get('user') + password
			return render(request,'error.html',{'error_message':error_message})
	else:
		error_message = 'This is not a valid request'
		return render(request,'error.html',{'error_message':error_message})

# def loginvalidate(request):
# 	if request.method=='POST':
# 		user = Profile.objects.get(email = request.POST.get('user'))
# 		if user.password == request.POST.get('password'):
# 			return HttpResponseRedirect(reverse('dash'))
# 		else:
# 			error_message = request.POST.get('user') + password
# 			return render(request,'error.html',{'error_message':error_message})
		
# 	else:
# 		error_message = 'This is not a valid request'
# 		return render(request,'error.html',{'error_message':error_message})


def secret(request):
	return render(request, 'll.html',{})

def signin(request):
	pass

def registrations(request):
	if not request.user.is_active():
    		return render(request,'regclosed.html',{})
	else:
		return render(request,'dash.html',{})
		
def checkpay(request):
	pass
#@login_required(redirect_field_name='loginpage')
def signup(request):
	if request.method == 'POST':
		# try:
		try:
			queryset = Profile.objects.get(email = request.POST.get('email'))
		# except User.DoesNotExist:
		# 	print('ok')
		#print(form.errors)
		except Profile.DoesNotExist:
			#print (form.data['username'])
			
			user = User(username=request.POST.get('email'), password = 'AcumenItfest')

			qrcode = get_random_string(5).lower()
			# user.is_active = True
			user.save()
			# current_site = get_current_site(request)
			# domain = current_site.domain
			# uid = urlsafe_base64_encode(force_bytes(user.pk))
			# uid1 = force_text(urlsafe_base64_decode(uid))
			# token = account_activation_token.make_token(user)
			sample = pyq.create(qrcode)
			# print(sample)
			sample.png(qrcode+'.png',scale = 6)
		
			# print(uid)
			username = request.POST.get('username')
			password = request.POST.get('password')
			emailid = request.POST.get('email')
			phone = request.POST.get('phone')
			college = request.POST.get('college')
			roll  = request.POST.get('roll')
			branch = request.POST.get('branch')
			year = request.POST.get('year')
			events = request.POST.getlist('q3')
			#print(events)
			mail_subject = 'Activate your AcumenIT account.'
			message = render_to_string('acc_active_email.html', {
				'qrcode' : qrcode
			})
			# print(str('http://'+ "www.acumenit.in" +"/" +"activate" + "/" + str(uid.decode('utf-8')) + "/" + str(token)))
			email = EmailMessage(
						mail_subject, message, to=[emailid]
			)

			# email.attach(qrcode+'.png',sample.png(qrcode+'.png',scale=6),'image/png')
			# email.attach(sample.name,sample.read)
			email.attach_file(qrcode+'.png')
			email.send()
			image_data = open(qrcode+'.png', "rb").read()
			
			# userobj = User.objects.get(username=emailid)

			# print(userobj.password)

			obj = Profile(QId = qrcode,user = user,email = emailid, 
			College = college, Branch = branch, Phone_number = phone,
			roll = roll,name = username, password = password)
			obj.save()

			nobj = RegistrationsAndParticipations(QId = obj, registered = events, paid = [], participated = [])
			nobj.save()

			return HttpResponseRedirect(reverse('loginpage'))
			
		else:
			messages.info(request, 'User/Email already Exists')
			return render(request, 'registrations.html',{})
	else:
		#form = SignupForm()
		return render(request, 'registrations.html',{})
	
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		print(uid)
		user = User.objects.get(pk=uid)
		print(user)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None:
		user.is_active = True
		user.save()
		login(request, user)
		#return redirect('home')
		#return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
		return HttpResponseRedirect(reverse('loginpage'))
	else:
		return HttpResponse('Activation link is invalid!')

def test(request):
	error_message = get_random_string(5).lower()

	return HttpResponse(error_message, content_type='text/plain')
def signupconfirm(request):
    return HttpResponse("success")

def social(request):
	return render(request, 'social.html',{})

def sponsors(request):
	return render(request, 'sponsors.html',{})


def team(request):
	return render(request, 'team.html',{})

def dash(request):
	user_set = User.objects.get(username = request.user)
	queryset = Profile.objects.get(user = user_set)
	qrcode = queryset.QId
	image_data = open(qrcode+'.png', "rb").read()
	return HttpResponse(image_data,content_type='image/png')
# def dash(request):
# 	pass

# def usersubmit(request):
# 	if request.method == 'POST':
# 		if request.user is not none and request.user.is_active():
# 			UserDetails = Profile.object.filter(user = request.user)
# 			RegistrationStatus =RegistrationsAndParticipations.objects.filter(QId = UserDetails.QId )
# 			RegistrationStatus.registered  = request.POST.get('registered') 
# 			RegistrationStatus.save()
# 			return redirect(reverse('dash'))
# 		else:
# 			return redirect(reverse('loginpage'))
# 	else:
# 		return HttpResponse("Invalid Response Type")
def usersubmit(request):
	pass

# def Pay(request):
# 	#this is where payment goes to
# 	return render(request,'payment.html',{})
def Pay(request):
	pass

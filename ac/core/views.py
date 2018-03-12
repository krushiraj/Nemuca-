from django.shortcuts import render, redirect


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
		user = request.POST.get('user')
		print(user)
		password = request.POST.get('password')
		print(password)
		user = authenticate(username = user, password = password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('dash'))
		else:
			error_message = 'invalid credentials'
			return render(request,'error.html',{'error_message':error_message})
	else:
		error_message = 'This is not a valid request'
		return render(request,'error.html',{'error_message':error_message})

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
		form = SignupForm(data=request.POST)
		print (form.is_valid())
		print(form.errors)
		if form.is_valid():
			print (form.data['username'])
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			domain = current_site.domain
			uid = urlsafe_base64_encode(force_bytes(user.pk))
			uid1 = force_text(urlsafe_base64_decode(uid))
			token = account_activation_token.make_token(user)
			userobj = User.objects.get(pk=uid1)
			qrcode = get_random_string(5).lower()
			obj = Profile(QId = qrcode,user = userobj,)
			obj.save()
			mail_subject = 'Activate your AccumenIT account.'
			message = render_to_string('acc_active_email.html', {
				'activate_url' : str('http://'+ "www.acumenit.in" +"/" +"activate" + "/" + str(uid.decode('utf-8')) + "/" + str(token)) ,
				'qrcode' : qrcode
			})
			print ('http://'+ str(domain) +"/" +"activate" + "/" + str(uid.decode('utf-8')) + "/" + str(token))
			to_email = form.cleaned_data.get('username')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			email.send()
			return HttpResponse("Check your email")
		else:
			return HttpResponse(form.errors)
	else:
		form = SignupForm()
	return render(request, 'registrations.html', {'form': form})

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		print(uid)
		user = User.objects.get(pk=uid)
		print(user)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		#return redirect('home')
		#return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
		return redirect(reverse('dash'))
	else:
		return HttpResponse('Activation link is invalid!')
def test(request):
	error_message = get_random_string(5).lower()

	return HttpResponse(error_message, content_type='text/plain')
def signupconfirm(request):
    return HttpResponse("success")

#@login_required(redirect_field_name='loginpage')
def social(request):
	return render(request, 'social.html',{})

#@login_required(redirect_field_name='loginpage')
def sponsors(request):
	return render(request, 'sponsors.html',{})

#@login_required(redirect_field_name='loginpage')
def team(request):
	return render(request, 'team.html',{})

@login_required(redirect_field_name = "loginpage")
def dash(request):
	user_set = User.objects.get( username = request.user )
	try:
		queryset = Profile.objects.get(user = user_set)
	except Profile.DoesNotExist:
		queryset = None

	if queryset:
		QrCode = queryset.QId
		eventdetails = RegistrationsAndParticipations.objects.filter(QId = queryset )
		FirstName = request.user.first_name
		Year = queryset.Year
		Phone = queryset.Phone_number
		Branch = queryset.Branch
		College = queryset.College
		paid = eventdetails.paid  
		registered = eventdetails.registered
		# Not needed participated = eventdetails.participated

		return render(request, 'dash.html',{'FirstName':FirstName
		,'Year':Year,'Phone':Phone,'Branch':Branch,'College':College,'paid':paid,'registered':registered})
	else:
		return HttpResponseRedirect(reverse('loginpage'))
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

import pyrebase
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

firebaseConfig = {
    #put here firebase config info
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signin(request):
	return render(request,"main/signin.html")

def postsignin(request):
	email=request.POST.get('email')
	passw=request.POST.get('password')
	#print(request)
	#print(email)
	try:
		user=auth.sign_in_with_email_and_password(email,passw)
		
	except:
		message="Invalid Credentials"
		messages.error(request,message)
		return redirect('/signin')
	return render(request,'main/welcome.html',{"e":email})

def reset(request):
	return render(request,'main/reset.html')

def postreset(request):
	email=request.POST.get('email')
	try:
		auth.send_password_reset_email(email)
	except:
		return redirect('/register')
		messages.error(request,"email not registered")
	return redirect('/signin')
	return HttpResponse("Link sent Successfully")

def register(request):
	return render(request,"main/register.html")

def postregister(request):
	email=request.POST.get('email')
	passw=request.POST.get('password')
	print(email)
	try:
		user = auth.create_user_with_email_and_password(email,passw)
		#user = auth.refresh(user['refreshToken'])
		#user['idToken']
		auth.send_email_verification(user['idToken'])
	except:
		message="Invalid Credentials"
		return redirect('/register')
	return HttpResponse("Account Successfully Created")

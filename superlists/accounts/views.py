import sys
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render

# Create your views here.
def login(request):
	print('login view', file=sys.stderr)
	user = authenticate(asseertion=request.POST['assertion'])
	if user is not None:
		auth_login(request, user)
	return redirect('/')

def logout(request):
	auth_logout(request)
	return redirect('/')
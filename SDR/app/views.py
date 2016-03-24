from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
import json

def login(request):
	context = {}
	return render(request, "login/login.html")
	pass

def validarLogin(request):
	resp = {}
	try:
		if request.method == 'POST':
			resp["sms"] = 1;
		else:
			resp["sms"] = 2;
		return HttpResponse(json.dumps(resp))
	except Exception:
		return HttpResponse(json.dumps({"sms":"3"}))	
	pass	
		
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import json

def index(request):
	try:
		context = {}
		if request.user.is_authenticated():
			return HttpResponseRedirect('/menu')
		else:	
			return render(request, "login/login.html")
		pass
	except Exception:
		return HttpResponse("Se ha Producido un error: 404")
	pass

def validarLogin(request):
	resp = {}
	try:
		if request.method == 'POST':
			user = request.POST["username"];
			password = request.POST["password"];
			access = False;
			if user == "" or password == "":
				resp["sms"] = "2";
			else:
				resp["username"] = user;
				access = authenticate(username = user, password = password);
				if access is not None:
					if access.is_active:
						login(request, access)
						resp["username"] = access.first_name +" "+ access.last_name;
						resp["sms"] = "1";
					else:
						resp["sms"] = "4";	
				else:
					resp["sms"] = "3";
		else:
			resp["sms"] = "6";
		return HttpResponse(json.dumps(resp))
	except Exception:
		return HttpResponse(json.dumps({"sms":"-1"}))
	pass

def menu(request):
	try:
		if request.user.is_authenticated():
			context = {}
			return render(request, "menus/menu.html", context)
		else:
			return HttpResponseRedirect("/")	
		pass
	except Exception:
		return HttpResponse(str("Error! no se ha podido cargar la pagina.."))
	pass

def closeSession(request):
	try:
		logout(request)
		return HttpResponseRedirect("/")
	except Exception:
		return HttpResponse(str("Se ha producido un error 404"))
	pass			
		
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import json, re

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
				resp["username"] = user
				arraylongin = {}
				if validarEmail(user):
					query = User.objects.filter(email=user).values_list("username", flat = True)
					arraylongin = {"username":query, "password":password}
				else:
					arraylongin = {"username":user, "password":password}
					pass
				access = authenticate(**arraylongin);	
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

def validarEmail(email):
	try:
		if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()):
			return True
		else:
			return False	
	except Exception:
		print("Error Validando")
		return False
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
		return HttpResponse(str("Se ha producido un error 404."))
	pass

def newUser(request):
	try:
		if request.user.is_authenticated():
			context = {"newuser":'Nuevo Usuario'}
			return render(request,"configuracion/new-user.html", context)
		else:
			return HttpResponseRedirect("/")
		pass
	except Exception:
		return HttpResponse("Se ha producido un error 404.")
	pass				

def changeRoles(request):
	try:
		query = Group.objects.all();
		select = "";
		for x in query:
			select += "<option value="+str(x.id)+">"+x.name+"</option>"; 
			pass
		return HttpResponse(select);	
		pass
	except Exception:
		return HttpResponse("-1")
	pass

def saveUser(request):
	try:
		if request.method == "POST":
			firstname = request.POST["first_name"]
			lastname = request.POST["last_name"]
			username = request.POST["username"]
			password = request.POST["password"]
			email = request.POST["email"]
			rol = request.POST["rol"]
			idUser = request.POST["user"]
			resp = {};
			cont = User.objects.filter(email=email).count();
			if cont > 0 and idUser == "":
				resp["sms"] = 2;
			elif idUser != "":

				pass
			else:

				pass	

			return HttpResponse("hola")
		else:
			return HttpResponse("6")	
		pass
	except Exception:
		return HttpResponse("-1")
	pass		
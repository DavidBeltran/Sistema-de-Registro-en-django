from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.db.models import Q
from app.models import AuthUserGroups, AuthUser, AuthGroup
from datetime import datetime
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
			if "password" in request.POST:
				password = request.POST["password"]
				pass	
			email = request.POST["email"]
			rol = request.POST["rol"]
			idUser = request.POST["user"]
			roles = False
			resp = {};
			fecha = datetime.now()
			count = User.objects.filter(Q(email=email) | Q(username=username)).count();
			if rol == 1: 
				roles = True 
			else: 
				roles = False
			if idUser != "":
				count = User.objects.filter(Q(id=idUser) & (Q(email=email) | Q(username=username)));
				if str(idUser) == str(count[0].id):
					User.objects.filter(id = idUser).update(email=email, username=username, last_name=lastname, first_name=firstname, is_superuser=roles);
					resp["sms"] = 2
				else:
					resp["sms"] = 1;	
			elif count > 0 and idUser == "":	
				resp["sms"] = 1;
			else:
				user = User(username=username, email=email, last_name=lastname, first_name=firstname, is_active=False, is_staff=False, is_superuser=roles, date_joined=fecha)
				user.set_password(password)
				if user.save() is None:
					objetoRoles = AuthGroup.objects.get(id=rol);
					objetoUser = AuthUser.objects.get(email=email)
					AuthUserGroups(user=objetoUser, group=objetoRoles).save()
					resp["sms"] = 3
				else:
					resp["sms"] = 4
				pass
			return HttpResponse(json.dumps(resp))
		else:
			return HttpResponse("-1")	
			pass
	except Exception:
		return HttpResponse("-1")
		pass

def newUser(request):
	try:
		if request.user.is_authenticated():
			context = {"newuser":'Nuevo Usuario', "idUser":"", "first_name":"", "last_name":"", "email":"", "username":"", "password":"", "rol":""}
			return render(request,"configuracion/new-user.html", context)
		else:
			return HttpResponseRedirect("/")
		pass
	except Exception:
		return HttpResponse("Se ha producido un error 404.")
	pass

def updateUSer(request):
	try:
		if request.user.is_authenticated():
			if "id" in request.GET:
				idUser = request.GET["id"]
				query = AuthUserGroups.objects.filter(user=idUser)
				context = {"newuser":'Actualizar Usuario', "idUser":idUser, "first_name":query[0].user.first_name, "last_name":query[0].user.last_name, "email":query[0].user.email, "username":query[0].user.username, "rol":query[0].group.id}
			else:
				context = {"newuser":'Actualizar Usuario', "idUser":request.user.id, "rol":request.user.groups.all()[0].id,"password":request.user.password,"username":request.user.username,"email":request.user.email,"last_name":request.user.last_name,"first_name":request.user.first_name}
			return render(request,"configuracion/new-user.html", context)
		else:
			return HttpResponseRedirect("/")
		pass
	except Exception:
		return HttpResponse("Se ha producido un error 404.")
	pass


def searchUser(request):
	try:
		if request.user.is_authenticated():
			context = {}
			return render(request,"configuracion/search-user.html", context)
		else:
			return HttpResponseRedirect("/")	
		pass
	except Exception:
		return HttpResponse("Se ha producido un error 404.")
	pass


def searchUserTable(request):
	try:
		query = AuthUserGroups.objects.all();
		paginacion = Paginator(query, 10)
		if "index" in request.GET:
			pagina = int(request.GET["index"])
		else:
			pagina = int(1)
		pagination = paginacion.page(pagina)	
		context = {"pagination":pagination}
		html = render(request, "configuracion/tabla-user.html", context)
		return html
		pass
	except Exception:
		return HttpResponse("Se ha producido un error 404.")
	pass			
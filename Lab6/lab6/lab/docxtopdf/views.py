from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo, PDFConverter
from django.views.generic import CreateView

def index(request):
	return render(request, "index.html")
	
def users(request):
    users = UserInfo.objects.all()
    return render(request, "users.html", context={"users": list(users)})
	
def userInfo(request, id):
    userInfo = PDFConverter.objects.filter(id=id).values()
    username = UserInfo.objects.filter(id=list(userInfo)[0]['user_id']).values()
    return render(request, "userInfo.html", context={"userInfo": list(userInfo)[0], "username": list(username)[0]})

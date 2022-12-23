from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("main index")

def Adminhome(request):
    mail = (request.POST.get('LoginEmail', 'default'))
    pas = (request.POST.get('loginPassword', 'default'))
    if mail == 'admin@gmail.com' and pas == 'admin':
        return render(request, 'Admin-home.html')
    else:
        return render(request, 'index.html')
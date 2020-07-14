from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def addUser(request):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    postEmail = request.POST['email']
    postAge = request.POST['age']
    newUser = User.objects.create(name=firstName + ' ' + lastName, email=postEmail, age=postAge)
    return redirect('/')
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('@#$%^&*()'))
    if request.GET.get('digits'):
        characters.extend(list('123456789'))


    length = int(request.GET.get('length',12))

    dummyPass = ''
    for x in range(length):
        dummyPass+=random.choice(characters) 


    return render(request,'generator/password.html',{'password':dummyPass})


def about(request):
    return render(request,'generator/about.html')
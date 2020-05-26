from django.shortcuts import render

import datetime

def home(request):
    return render(request, 'base.html')

def other(request):
    context= {
        'k1':'Welcome to the Second Page',
        }
    return render(request,'others.html',context)


def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html',{'time': time})

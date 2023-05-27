from django.shortcuts import render
from app.forms import *
from app. models import *
from django.http import HttpResponse
# Create your views here.


def TOWOAO(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessrecordsForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessrecordsForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            tnfd=tfd.save(commit=False)
            tnfd.save()
            wnfd=wfd.save(commit=False)
            wnfd.topic_name=tnfd
            wnfd.save()
            anfd=afd.save(commit=False)
            anfd.name=wnfd
            anfd.save()
            return HttpResponse('successfully submitted ...... ')
        else:
            return HttpResponse('invalid data ')
            


    return render(request,'web.html',d)


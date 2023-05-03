from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    d={'tfo':TopicForm(),'wfo':WebpageForm(),'afo':ARForm()}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=ARForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            nsto=tfd.save(commit=False)
            nsto.save()

            nswo=wfd.save(commit=False)
            nswo.topic_name=nsto
            nswo.save()
            
            nsaro=afd.save(commit=False)
            nsaro.name=nswo
            nsaro.save()
            return HttpResponse('registration successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'register.html',d)

   
  
      
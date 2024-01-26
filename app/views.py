from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('you are allowed to insert data')
        else:
            return HttpResponse('not allowed to insert data')
    return render(request,'create_student.html',d)
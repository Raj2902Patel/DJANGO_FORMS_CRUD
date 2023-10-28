from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from .forms import *
from .models import *

def home(request):
    if request.method == 'POST':
        data_form = StudentForm(request.POST)

        if data_form.is_valid():
            data_form.save()
        return redirect('home')
    
    data_form = StudentForm()
    
    context = {'data_form':data_form}

    return render(request,'add.html',context)


def display(request):
    data_form = student.objects.all()

    return render(request,'display.html',{'data_form':data_form})


def single(request,id):
    data_form = get_object_or_404(student,pk=id)
    return render(request,'single.html',{'data_form':data_form})


def delete(request,id):
    data_form = get_object_or_404(student,pk=id)
    data_form.delete()
    return render(request,'delete.html')


def edit(request,id):
    data_form = get_object_or_404(student,pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=data_form)
        form.save()
        return redirect('display')
    else:
        form = StudentForm(instance=data_form)
    return render(request,'edit.html',{'form':form})
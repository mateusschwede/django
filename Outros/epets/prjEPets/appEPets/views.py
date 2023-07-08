from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    pets = Pet.objects.all()
    context = {'pets':pets}
    return render(request,'list.html',context)

def addPet(request):
    pets = Pet.objects.all()
    form = FormPet()
    context = {'pets':pets,'form':form}
    if request.method == "POST":
        form = FormPet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'add.html',context)

def detailPet(request,pk):
    context = {}
    context["pet"] = Pet.objects.get(id=pk)
    return render(request,'detail.html',context)

def deletePet(request,pk):
    pet = Pet.objects.get(id=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('/')
    context = {'pet':pet}
    return render(request,'delete.html',context)

def updatePet(request,pk):
    pet = Pet.objects.get(id=pk)
    form = FormPet(instance=pet)
    if request.method == "POST":
        form = FormPet(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'update.html',context)

def adotPet(request,pk):
    pet = Pet.objects.get(id=pk)
    if request.method == "POST":
        pet.adotado = True
        pet.save()
        return redirect('/adotado')
    context = {'pet':pet}
    return render(request,'adot.html',context)

def adotado(request):
    return render(request,'adotado.html')
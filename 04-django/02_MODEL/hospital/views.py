from django.shortcuts import render, redirect
from .models import Patient


def new(request):
    return render(request, 'hospital/new.html')


def create(request):
    patient = Patient()
    patient.name = request.POST['name']
    patient.age = request.POST['age']
    patient.height = request.POST['height']
    patient.weight = request.POST['weight']
    patient.mbti = request.POST['mbti']
    patient.save()
    return redirect('hospital:detail', patient.pk)


def index(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/index.html', {
        'patients': patients,
    })


def detail(request, pk):
    patient = Patient.objects.get(pk=pk)
    return render(request, 'hospital/detail.html', {
        'patient': patient,
    })


def edit(request, pk):
    patient = Patient.objects.get(pk=pk)
    return render(request, 'hospital/edit.html', {
        'patient': patient,
    })


def update(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.name = request.POST['name']
    patient.age = request.POST['age']
    patient.height = request.POST['height']
    patient.weight = request.POST['weight']
    patient.mbti = request.POST['mbti']
    patient.save()
    return redirect('hospital:detail', patient.pk)


def delete(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.delete()
    return redirect('hospital:index')    
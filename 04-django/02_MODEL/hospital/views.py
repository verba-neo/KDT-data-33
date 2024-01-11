from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

def new(request):
    form = PatientForm()
    return render(request, 'hospital/new.html', {
        'form': form,
    })


def create(request):
    form = PatientForm(request.POST)
    if form.is_valid():
        patient = form.save()
        return redirect('hospital:detail', patient.pk)
    else:
        return render(request, 'hospital/new.html', {
            'form': form,
        })


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
    form = PatientForm(instance=patient)

    return render(request, 'hospital/edit.html', {
        'patient': patient,
        'form': form,
    })


def update(request, pk):
    patient = Patient.objects.get(pk=pk)
    form = PatientForm(request.POST, instance=patient)
    if form.is_valid():
        patient = form.save()
        return redirect('hospital:detail', patient.pk)
    else:
        return render(request, 'hospital/edit.html', {
            'form': form,
        })


def delete(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.delete()
    return redirect('hospital:index')    
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Patient
from .forms import PatientForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('hospital:detail', patient.pk)
    else:
        form = PatientForm()
    return render(request, 'hospital/new.html', {
        'form': form,
    })


@require_safe
def index(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/index.html', {
        'patients': patients,
    })


@require_safe
def detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'hospital/detail.html', {
        'patient': patient,
    })


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save()
            return redirect('hospital:detail', patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital/edit.html', {
        'form': form,
    })


@require_POST
def delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('hospital:index')    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from .forms import RecordForm
from django.db.models import Q
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

@login_required
def record_list(request):
    query = request.GET.get('q')
    records = Record.objects.all()

    if query:
        records = records.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(quantity__icontains=query) |
            Q(birthdate__icontains=query)
        )

    return render(request, 'dk/record_list.html', {'records': records})

def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'dk/record_form.html', {'form': form, 'title': 'Edit Record'})

def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'dk/record_confirm_delete.html', {'record': record})

def record_create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'dk/record_form.html', {'form': form})
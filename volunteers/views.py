from django.shortcuts import render, redirect
from .models import Volunteer
from .forms import VolunteerForm

def register_volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteers:volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/register.html', {'form': form})

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/list.html', {'volunteers': volunteers})

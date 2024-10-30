from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Disaster  # Change to your Disaster model
from .forms import DisasterForm  # Change to your Disaster form
from django.core.paginator import Paginator
from django.contrib.auth import login
from .forms import RegisterForm

@login_required(login_url="/users/login")
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

@login_required(login_url="/users/login")
def disaster_list(request):
    disaster_queryset = Disaster.objects.all()

    # Set up pagination, 1000 items per page
    paginator = Paginator(disaster_queryset, 1000)

    # Get the current page number from the request
    page_number = request.GET.get('page', 1)

    # Get the corresponding page of disasters
    disasters_page = paginator.get_page(page_number)

    return render(request, "disasters/disaster_list.html", {"disasters": disasters_page})

@login_required(login_url="/users/login")
def create_disaster(request):
    if request.method == "POST":
        form = DisasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("disaster_list")
    else:
        form = DisasterForm()
    return render(request, "disasters/create_disaster.html", {"form": form})

@login_required(login_url="/users/login")
def update_disaster(request, pk):
    disaster = Disaster.objects.get(pk=pk)
    if request.method == "POST":
        form = DisasterForm(request.POST, instance=disaster)
        if form.is_valid():
            form.save()
            return redirect("disaster_list")
    else:
        form = DisasterForm(instance=disaster)
    return render(request, "disasters/update_disaster.html", {"form": form})

@login_required(login_url="/users/login")
def delete_disaster(request, pk):
    disaster = Disaster.objects.get(pk=pk)
    if request.method == "POST":
        disaster.delete()
        return redirect("disaster_list")
    return render(request, "disasters/delete_disaster.html", {"disaster": disaster})

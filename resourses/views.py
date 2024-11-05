from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource
from .forms import ResourceForm
from django.core.paginator import Paginator
from .forms import RegisterForm
from django.contrib.auth import login

@login_required(login_url="/users/login")
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect("index")  # Redirect to homepage or login
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def index(request):
    return render(request, 'index.html')

@login_required(login_url="/users/login")
def resource_list(request):
    resources = Resource.objects.all()
    paginator = Paginator(resources, 10)  # Show 10 resources per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "resources/resourse_list.html", {"page_obj": page_obj})

@login_required(login_url="/users/login")
def create_resource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("resource_list")
    else:
        form = ResourceForm()
    return render(request, "resources/create_resourse.html", {"form": form})

@login_required(login_url="/users/login")
def update_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect("resource_list")
    else:
        form = ResourceForm(instance=resource)
    return render(request, "resources/update_resourse.html", {"form": form})

@login_required(login_url="/users/login")
def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        resource.delete()
        return redirect("resource_list")
    return render(request, "resources/delete_resourse.html", {"resource": resource})


# Check if user is in the Admin group
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

# Check if user is in the Volunteer group
def is_volunteer(user):
    return user.groups.filter(name='Volunteer').exists()

# Restrict view to Admin users
@user_passes_test(is_admin)
def admin_only_view(request):
    pass

# Restrict view to Volunteer users
@user_passes_test(is_volunteer)
def volunteer_only_view(request):
    pass

from django.shortcuts import render, redirect
from users.decolators import is_admin, is_volunteer
from .forms import VolunteerRegistrationForm
from .models import Volunteer
from django.contrib.auth.decorators import user_passes_test

def register_volunteer(request):
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            role = form.cleaned_data['role']

            # Save volunteer information
            volunteer.save()
            return redirect('volunteers_list')
    else:
        form = VolunteerRegistrationForm()
    return render(request, 'volunteers/register.html', {'form': form})


def volunteer_list(request):
    volunteers = Volunteer.objects.all()  # Retrieve all volunteers
    return render(request, 'volunteers/list.html', {'volunteers': volunteers})


# View restricted to volunteers
@user_passes_test(is_volunteer)
def volunteers_list(request):
    # Show list of volunteers
    pass

# View restricted to admins
@user_passes_test(is_admin)
def manage_volunteers(request):
    # Allow admins to manage volunteers
    pass

# Check if user is in the Admin group
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

# Check if user is in the Volunteer group
def is_volunteer(user):
    return user.groups.filter(name='Volunteer').exists()

# Restrict view to Admin users
@user_passes_test(is_admin)
def admin_only_view(request):
    # view code for admins
    pass

# Restrict view to Volunteer users
@user_passes_test(is_volunteer)
def volunteer_only_view(request):
    # view code for volunteers
    pass


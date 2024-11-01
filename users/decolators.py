from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_volunteer(user):
    return user.groups.filter(name='Volunteer').exists()

def is_user(user):
    return user.groups.filter(name='User').exists()

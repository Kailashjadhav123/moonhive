from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Property, Tenant
from django.contrib.auth import authenticate, login, logout

def home(request):
    property_obj = Property.objects.all()
    tenant = Tenant.objects.all()
    context = {'property': property_obj, 'tenants': tenant}
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any desired page after successful login
        else:
            # Authentication failed, show an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('home'))
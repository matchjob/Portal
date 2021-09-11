
# django
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Exception
from django.db.utils import IntegrityError

# Models
from users.models import Profile as UserProfile
from company.models import ProfileCompany


def home_login(request):
    """Login view."""
    if request.user.is_authenticated:
        if UserProfile.objects.filter(user=request.user.id).exists():
            return HttpResponseRedirect(reverse('users:UsersHomePage'))
        elif ProfileCompany.objects.filter(user=request.user.id).exists():
            return HttpResponseRedirect(reverse('company:CompanyHomePage'))
        else:
            return HttpResponseRedirect(reverse('users:UsersHomePage'))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if UserProfile.objects.filter(user=user).exists():
                return HttpResponseRedirect(reverse('users:UsersHomePage'))
            elif ProfileCompany.objects.filter(user=user).exists():
                return HttpResponseRedirect(reverse('company:CompanyHomePage'))
            else:
                return HttpResponseRedirect(reverse('users:UsersHomePage'))

        else:
            return render(request, 'home/login.html', {'error': 'Invalid username and password'})
    else:
        return render(request, 'home/login.html')


class HomePage(TemplateView):
    """Pagina Principal"""
    template_name = "home/principal.html"

    def get_context_data(self, **kwargs):
        """ get context """
        args = dict()
        return args


def home_logout(request):
    """logout """
    logout(request)
    return HttpResponseRedirect(reverse('home:login'))


def signup(request):
    """logout """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        cedula = request.POST['cedula']

        if password != password_confirmation:
            return render(request, 'home/signup.html', {'error': 'Password confirmation does not match'})

        if User.objects.filter(email=email).exists():
            return render(request, 'home/signup.html', {'error': 'Email is already in use'})

        if UserProfile.objects.filter(cedula=cedula).exists():
            return render(request, 'home/signup.html', {'error': 'Cedula is already in use'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'home/signup.html', {'error': 'Username is already in use'})

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile = UserProfile(user=user, cedula=cedula)
        profile.save()

        return HttpResponseRedirect(reverse('home:login'))
    return render(request, 'home/signup.html')


def signup_company(request):
    """logout """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        comercial_name = request.POST['comercial_name']
        email = request.POST['email']
        cedula = request.POST['cedula']

        if password != password_confirmation:
            return render(request, 'home/signup_company.html', {'error': 'Password confirmation does not match'})

        if User.objects.filter(email=email).exists():
            return render(request, 'home/signup_company.html', {'error': 'Email is already in use'})

        if UserProfile.objects.filter(cedula=cedula).exists():
            return render(request, 'home/signup_company.html', {'error': 'Cedula is already in use'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'home/signup_company.html', {'error': 'Username is already in use'})

        user.first_name = ""
        user.last_name = ""
        user.email = email
        user.save()

        profile = ProfileCompany(user=user, cedula=cedula, comercial_name=comercial_name)
        profile.save()

        return HttpResponseRedirect(reverse('home:login'))
    return render(request, 'home/signup_company.html')

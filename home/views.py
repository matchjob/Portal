# django
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

#Models
from users.models import Profile as UserProfile


def home_login(request):
    """Login view."""
    if request.user.is_authenticated:
        pass
        # return HttpResponseRedirect(reverse('users:home'))
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if UserProfile.objects.filter(user=user).exists():
                return HttpResponseRedirect(reverse('users:UsersHomePage'))
            else:
                return HttpResponseRedirect(reverse('users:UsersHomePage'))

        else:
            return render(request, 'home/login.html')
    else:
        return render(request, 'home/login.html')


class HomePage(TemplateView):
    """Pagina Principal"""
    template_name = "home/principal.html"

    def get_context_data(self, **kwargs):
        args = dict()
        return args


def home_logout(request):
    """logout """
    logout(request)
    return HttpResponseRedirect(reverse('home:login'))
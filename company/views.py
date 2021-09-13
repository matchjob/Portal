
# django
from django.views.generic import TemplateView
from django.shortcuts import render

# Django Rest Framework

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# frameworks
from frameworks.frameworks import get_data_combos_profile, get_url_zone

# models
from profiles.models import *
from .models import ProfileCompany

# forms
from .forms import CompanyProfileForm

# Create your views here.


class CompanyHomePage(TemplateView):
    """Pagina Principal"""
    template_name = "company/home_company.html"

    def get_context_data(self, **kwargs):
        """ Obtiene datos del perfil"""
        menu_dict = dict()
        return menu_dict


def company_perfil_page(request):
    """Pagina Principal"""

    if request.method == "POST":
        profile = request.user.profilecompany
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.phone_number = data['phone_number']
            profile.web_site = data['web_site']
            profile.lat = data['lat']
            profile.lon = data['lon']
            profile.biography = data['biography']
            if data['picture']:
                profile.picture = data['picture']
            profile.save()

        dict_perfil = get_data_combos_profile(request.user.id)
        dict_perfil['map'] = get_url_zone(request.user.profilecompany.lat, request.user.profilecompany.lon)
        dict_perfil['form'] = form
        return render(request, 'company/company_perfil.html', dict_perfil)

    dict_perfil = get_data_combos_profile(request.user.id)
    dict_perfil['map'] = get_url_zone(request.user.profilecompany.lat, request.user.profilecompany.lon)
    form = CompanyProfileForm()
    dict_perfil['form'] = form
    return render(request, 'company/company_perfil.html', dict_perfil)


def company_new_match_page(request):
    """Pagina Principal"""
    if request.method == "POST":
        dict_perfil = get_data_combos_profile(request.user.id)
        dict_perfil['busqueda_realizada'] = 1
        return render(request, 'company/company_new_match.html', dict_perfil)
    else:
        dict_perfil = get_data_combos_profile(request.user.id)
        return render(request, 'company/company_new_match.html', dict_perfil)


class CompanyMatchPage(TemplateView):
    """Pagina Principal"""
    template_name = "company/company_match_realizados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class CompanyMatchPageAceptados(TemplateView):
    """Pagina Principal"""
    template_name = "company/company_match_aceptados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class CompanyMatchPageDeclinados(TemplateView):
    """Pagina Principal"""
    template_name = "company/company_match_declinados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class CompanyMatchPageRechazados(TemplateView):
    """Pagina Principal"""
    template_name = "company/company_match_rechazados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args
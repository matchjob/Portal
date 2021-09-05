# django
from django.views.generic import TemplateView
from django.shortcuts import render


class UsersHomePage(TemplateView):
    """Pagina Principal"""
    template_name = "users/home.html"
    def get_context_data(self, **kwargs):
        menu_dict = dict()
        return menu_dict


class UsersPerfilPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/perfil.html"
    def get_context_data(self, **kwargs):
        args = dict()
        return args


class UsersHVPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/hoja_vida.html"
    def get_context_data(self, **kwargs):
        args = dict()
        return args


class UsersMatchPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/match_realizados.html"
    def get_context_data(self, **kwargs):
        args = dict()
        return args


class UsersTestPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/test.html"
    def get_context_data(self, **kwargs):
        args = dict()
        return args

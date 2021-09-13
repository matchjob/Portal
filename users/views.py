
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
from .models import Profile, UserSkills, UserLanguages, UserSoftSkills
from profiles.models import *

# forms
from .forms import ProfileForm


class UsersHomePage(TemplateView):
    """Pagina Principal"""
    template_name = "users/home.html"

    def get_context_data(self, **kwargs):
        """ Obtiene datos del perfil"""
        menu_dict = dict()
        menu_dict['profile'] = list(Profile.objects.values().filter(id=self.request.user.profile.id))
        return menu_dict


def users_perfil_page(request):
    """Pagina Principal"""

    if request.method == "POST":
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data['department']:
                profile.department = Department.objects.get(id=data['department']['id'])
            if data['department']:
                profile.specialism = Specialism.objects.get(id=data['specialism']['id'])
            profile.currently_working = data['currently_working']
            profile.search_job = data['search_job']
            profile.home_office = data['home_office']
            profile.freelancer = data['freelancer']
            profile.residence_change = data['residence_change']
            profile.remote_work = data['remote_work']
            profile.to_travel = data['to_travel']
            profile.desired_salary = data['desired_salary']
            profile.current_salary = data['current_salary']
            profile.phone_number = data['phone_number']
            profile.web_site = data['web_site']
            profile.lat = data['lat']
            profile.lon = data['lon']
            profile.biography = data['biography']
            if data['country']:
                profile.country = Country.objects.get(id=data['country']['id'])
            profile.nearby_search = data['nearby_search']
            profile.gender = data['gender']
            profile.academic_title = data['academic_title']
            if data['picture']:
                profile.picture = data['picture']
            profile.save()

        dict_perfil = get_data_combos_profile(request.user.id)
        dict_perfil['map'] = get_url_zone(request.user.profile.lat, request.user.profile.lon)
        dict_perfil['form'] = form
        return render(request, 'users/perfil.html', dict_perfil)

    dict_perfil = get_data_combos_profile(request.user.id)
    dict_perfil['map'] = get_url_zone(request.user.profile.lat, request.user.profile.lon)
    form = ProfileForm()
    dict_perfil['form'] = form
    return render(request, 'users/perfil.html', dict_perfil)


def users_hoja_vida_page(request):
    """Pagina Principal"""

    if request.method == "POST":
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data['department']:
                profile.department = Department.objects.get(id=data['department']['id'])
            if data['department']:
                profile.specialism = Specialism.objects.get(id=data['specialism']['id'])
            profile.currently_working = data['currently_working']
            profile.search_job = data['search_job']
            profile.home_office = data['home_office']
            profile.freelancer = data['freelancer']
            profile.residence_change = data['residence_change']
            profile.remote_work = data['remote_work']
            profile.to_travel = data['to_travel']
            profile.desired_salary = data['desired_salary']
            profile.current_salary = data['current_salary']
            profile.phone_number = data['phone_number']
            profile.web_site = data['web_site']
            profile.lat = data['lat']
            profile.lon = data['lon']
            profile.biography = data['biography']
            if data['country']:
                profile.country = Country.objects.get(id=data['country']['id'])
            profile.nearby_search = data['nearby_search']
            profile.gender = data['gender']
            profile.academic_title = data['academic_title']
            if data['picture']:
                profile.picture = data['picture']
            profile.save()

        dict_perfil = get_data_combos_profile(request.user.id)
        dict_perfil['map'] = get_url_zone(request.user.profile.lat, request.user.profile.lon)
        dict_perfil['form'] = form
        return render(request, 'users/hoja_vida.html', dict_perfil)

    dict_perfil = get_data_combos_profile(request.user.id)
    dict_perfil['map'] = get_url_zone(request.user.profile.lat, request.user.profile.lon)
    form = ProfileForm()
    dict_perfil['form'] = form
    return render(request, 'users/hoja_vida.html', dict_perfil)


class UsersHVPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/hoja_vida.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class UsersMatchPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/match_realizados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class UsersMatchPageAceptados(TemplateView):
    """Pagina Principal"""
    template_name = "users/match_aceptados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class UsersMatchPageDeclinados(TemplateView):
    """Pagina Principal"""
    template_name = "users/match_declinados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class UsersMatchPageRechazados(TemplateView):
    """Pagina Principal"""
    template_name = "users/match_rechazados.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class UsersEvolutionPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/crecimientos.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


class UsersTestPage(TemplateView):
    """Pagina Principal"""
    template_name = "users/test.html"

    def get_context_data(self, **kwargs):
        """ context """
        args = dict()
        return args


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_skill(request):
    """Agrega una Habilidad """

    skill = request.POST['skill']
    level = request.POST['skill_level']
    skill = skill.lower()
    skill = skill.strip()
    skill = skill.replace("  ", " ")

    if Skills.objects.filter(name=skill).exists():
        skill_object = Skills.objects.get(name=skill)
    else:
        skill_object = Skills.objects.create(name=skill)

    level_object = Level.objects.get(id=int(level))
    profile_object = request.user.profile

    if UserSkills.objects.filter(skill=skill_object.id, profile=profile_object.id).exists():
        UserSkills.objects.filter(skill=skill_object.id, profile=profile_object.id).update(level=level_object)
        return Response("Habilidad Actualizada Con Exito")
    else:
        UserSkills.objects.create(skill=skill_object, profile=profile_object, level=level_object)
    return Response("Habilidad Agregada Con Exito")


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_soft_skill(request):
    """Agrega una Habilidad """

    soft_skill = request.POST['soft_skill']
    level = request.POST['soft_skill_level']
    soft_skill = soft_skill.lower()
    soft_skill = soft_skill.strip()
    soft_skill = soft_skill.replace("  ", " ")

    if SoftSkill.objects.filter(name=soft_skill).exists():
        soft_skill_object = SoftSkill.objects.get(name=soft_skill)
    else:
        soft_skill_object = SoftSkill.objects.create(name=soft_skill)

    level_object = Level.objects.get(id=int(level))
    profile_object = request.user.profile

    if UserSoftSkills.objects.filter(SoftSkill=soft_skill_object.id, profile=profile_object.id).exists():
        UserSoftSkills.objects.filter(SoftSkill=soft_skill_object.id, profile=profile_object.id).update(level=level_object)
        return Response("Habilidad Blanda Actualizada Con Exito")
    else:
        UserSoftSkills.objects.create(SoftSkill=soft_skill_object, profile=profile_object, level=level_object)
    return Response("Habilidad Blanda Agregada Con Exito")


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_language(request):
    """Agrega una Habilidad """

    language = request.POST['language']
    level = request.POST['language_level']
    language = language.lower()
    language = language.strip()
    language = language.replace("  ", " ")

    if Language.objects.filter(name=language).exists():
        language_object = Language.objects.get(name=language)
    else:
        language_object = Language.objects.create(name=language)

    level_object = Level.objects.get(id=int(level))
    profile_object = request.user.profile

    if UserLanguages.objects.filter(language=language_object.id, profile=profile_object.id).exists():
        UserLanguages.objects.filter(language=language_object.id, profile=profile_object.id).update(level=level_object)
        return Response("Idioma Actualizado Con Exito")
    else:
        UserLanguages.objects.create(language=language_object, profile=profile_object, level=level_object)
    return Response("Idioma Agregado Con Exito")

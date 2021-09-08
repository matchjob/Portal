# Models
from profiles.models import Language, Department, Specialism, Skills, SoftSkill, Level, Country
from users.models import Profile, UserSkills, UserLanguages, UserSoftSkills


def get_checkbox_value(value):
    """Da formato al valor obtenido del formulario"""
    if value == 'on':
        value = True
    else:
        value = False
    return value


def get_url_zone(lat, lon):
    """obtiene el mapa de maps"""
    if lat:
        return "https://www.google.com.mx/maps/@" + str(lat) + "," + str(lon) + "z"
    elif lat == '':
        return None
    else:
        return None


def get_data_combos_profile(user_id):
    """obtiene combos para llenar perfil"""
    dict_perfil = dict()
    dict_perfil['Department'] = Department.objects.values().filter()
    dict_perfil['Specialism'] = Specialism.objects.values().filter()
    dict_perfil['Level'] = Level.objects.values().filter()
    dict_perfil['Country'] = Country.objects.values().filter()

    dict_perfil['skills'] = list(
        UserSkills.objects.values('skill__name', 'skill__id', 'level__level', 'level__id').filter(
            profile__user__id=user_id))
    dict_perfil['softskills'] = list(
        UserSoftSkills.objects.values('SoftSkill__name', 'SoftSkill__id', 'level__level', 'level__id').filter(
            profile__user__id=user_id))
    dict_perfil['languages'] = list(
        UserLanguages.objects.values('language__name', 'language__id', 'level__level', 'level__id').filter(
            profile__user__id=user_id))

    return dict_perfil
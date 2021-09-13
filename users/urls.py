"""Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='UsersHomePage',
        view=views.UsersHomePage.as_view(),
        name='UsersHomePage'
    ),
    path(
        route='UsersPerfilPage',
        view=views.users_perfil_page,
        name='UsersPerfilPage'
    ),
    path(
        route='UsersHVPage',
        view=views.users_hoja_vida_page,
        name='UsersHVPage'
    ),
    path(
        route='UsersMatchPage',
        view=views.UsersMatchPage.as_view(),
        name='UsersMatchPage'
    ),
    path(
        route='UsersMatchPageAceptados',
        view=views.UsersMatchPageAceptados.as_view(),
        name='UsersMatchPageAceptados'
    ),
    path(
        route='UsersMatchPageDeclinados',
        view=views.UsersMatchPageDeclinados.as_view(),
        name='UsersMatchPageDeclinados'
    ),
    path(
        route='UsersMatchPageRechazados',
        view=views.UsersMatchPageRechazados.as_view(),
        name='UsersMatchPageRechazados'
    ),
    path(
        route='UsersTestPage',
        view=views.UsersTestPage.as_view(),
        name='UsersTestPage'
    ),
    path(
        route='UsersEvolutionPage',
        view=views.UsersEvolutionPage.as_view(),
        name='UsersEvolutionPage'
    ),
    path(
        route='add_skill',
        view=views.add_skill,
        name='add_skill'
    ),

    path(
        route='add_soft_skill',
        view=views.add_soft_skill,
        name='add_soft_skill'
    ),

    path(
        route='add_language',
        view=views.add_language,
        name='add_language'
    ),

]

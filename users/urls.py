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
        view=views.UsersPerfilPage.as_view(),
        name='UsersPerfilPage'
    ),
    path(
        route='UsersHVPage',
        view=views.UsersHVPage.as_view(),
        name='UsersHVPage'
    ),
    path(
        route='UsersMatchPage',
        view=views.UsersMatchPage.as_view(),
        name='UsersMatchPage'
    ),
    path(
        route='UsersTestPage',
        view=views.UsersTestPage.as_view(),
        name='UsersTestPage'
    ),

]

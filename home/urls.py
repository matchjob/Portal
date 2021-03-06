"""Users URLs."""

# Django
from django.urls import path

# View
from home import views


urlpatterns = [
    path(
        route='',
        view=views.HomePage.as_view(),
        name='HomePage'
    ),
    path(
        route='login/',
        view=views.home_login,
        name='login'
    ),
    path(
        route='logout/',
        view=views.home_logout,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='signup_company/',
        view=views.signup_company,
        name='signup_company'
    ),
]

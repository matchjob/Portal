"""Users URLs."""

# Django
from django.urls import path

# View
from home import views


urlpatterns = [

    # Management
    path(
        route='',
        view=views.HomePage.as_view(),
        name='HomePage'
    ),
]

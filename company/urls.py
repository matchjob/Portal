"""Users URLs."""

# Django
from django.urls import path

# View
from company import views


urlpatterns = [

    # Management
    path(
        route='CompanyHomePage',
        view=views.CompanyHomePage.as_view(),
        name='CompanyHomePage'
    ),
    path(
        route='CompanyPerfilPage',
        view=views.company_perfil_page,
        name='CompanyPerfilPage'
    ),
    path(
        route='CompanyNMPage',
        view=views.company_new_match_page,
        name='CompanyNMPage'
    ),
    path(
        route='CompanyMatchPage',
        view=views.CompanyMatchPage.as_view(),
        name='CompanyMatchPage'
    ),


]

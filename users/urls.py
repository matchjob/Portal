"""Users URLs."""

# Django
from django.urls import path
from rest_framework.routers import DefaultRouter

# View
from users import views
from .views import ElementViewSet

router = DefaultRouter()
router.register(r'testroute', ElementViewSet)

urlpatterns = router.urls

urlpatterns += [

    # Management
    path(
        route='login/',
        view=views.login,
        name='login'
    ),
]
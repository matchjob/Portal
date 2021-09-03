# Django Rest Framework

from rest_framework.decorators import api_view, action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
#django
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
def login(request):
    """Login de API"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario Invalido')

    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return Response('Contraseña Invalida')

    token, create = Token.objects.get_or_create(user=user)

    return Response(token.key)


class ElementViewSet(viewsets.ModelViewSet):
    """test"""
    queryset = User.objects.values()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = User.objects.values()
        return Response(queryset)
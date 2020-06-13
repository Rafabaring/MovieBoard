# Importing rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import BaseUserManager

# Importing models
from create_user_app.models import Recommender
from movie_board_app.models import Genre

# Importing UserProfileSerializer
from create_user_app import serializers




# ========================================

class UserList(APIView):
    def get(self, request):
        all_users = Recommender.objects.all()
        users_serializer = serializers.CreateUserSerializer(all_users, many = True)

        return Response(users_serializer.data)


    def post(self, request):
        users_serializer = serializers.CreateUserSerializer(data = request.data)
        print(users_serializer)

        # .is_valid() verifica se o serializer segue os parâmetros iniciais. Nesse caso, max_length = 10
        if users_serializer.is_valid():
            print('serializer valido')
            users_serializer.save()
            return Response(users_serializer.data)

        else:
            print('serializer NOT valid')
            return Response(users_serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST)






class GenreList(APIView):
    def get_genre_list():
        all_genre = Genre.objects.all()
        return all_genre

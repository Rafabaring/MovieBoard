# Importing rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

# Importing models
from create_user_app.models import Recommender

# Importing serializer
from create_user_app.serializers import CreateUserSerializer

# List all stocks or create a new one
class UserList(APIView):

    def get(self, request):
        all_users = Recommender.objects.all()
        users_serializer = CreateUserSerializer(all_users, many = True)

        return Response(users_serializer.data)


    def post(self, request):
        users_serializer = CreateUserSerializer(data = request.data)
        print(users_serializer)

        # .is_valid() verifica se o serializer segue os parâmetros iniciais. Nesse caso, max_length = 10
        if users_serializer.is_valid():
            print('serializer valido')
            users_serializer.save()
            return Response(users_serializer.data)

        # Se o dado não for valid (acima), vai retornar um http bad request
        else:
            return Response(
                    users_serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )

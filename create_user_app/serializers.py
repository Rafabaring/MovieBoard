from rest_framework import serializers
from create_user_app.models import Recommender


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommender
        fields = '__all__'

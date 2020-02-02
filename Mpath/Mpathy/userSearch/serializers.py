from rest_framework import serializers
from userSearch.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Account
        fields = ('user_name','pass_wd','email','description','create_date')


class SuperviseeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisee
        fields = '__all__'

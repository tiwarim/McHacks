from rest_framework import serializers
from userSearch.models  import User_Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Account
        fields = ('user_name','pass_wd','email','description','create_date')

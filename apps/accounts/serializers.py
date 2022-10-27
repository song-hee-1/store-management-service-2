from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from apps.accounts.models import User

from django.core.validators import RegexValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CustomRegisterSerializer(RegisterSerializer):
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = serializers.CharField(validators=[phoneNumberRegex],
                                         help_text="휴대폰 번호는 다음과 같은 형식을 따라야 합니다: 010-1234-5678")
    date_of_birth = serializers.DateField()

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get('phone_number')
        user.date_of_birth = self.data.get('date_of_birth')
        user.save()
        return user

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

    def create_user(self, username, email, phone_number, date_of_birth, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수로 입력해야 합니다.')
        email = self.normalize_email(email)
        if not username:
            raise ValueError('이름은 필수로 입력해야 합니다.')
        if not phone_number:
            raise ValueError('휴대폰 번호는 필수로 입력해야 합니다.')
        if not date_of_birth:
            raise ValueError('생년월일은  필수로 입력해야 합니다.')
        user = self.model(
            email=email, username=username, phone_number=phone_number, date_of_birth=date_of_birth, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone_number, date_of_birth, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser는 is_staff = True이어야 합니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser는 is_superuser = True이어야 합니다.')
        return self.create_user(email, username, phone_number, date_of_birth, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=40, unique=False)
    email = models.EmailField(unique=True, max_length=250)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=13, unique=True,
                                    help_text="휴대폰 번호는 다음과 같은 형식을 따라야 합니다: 010-1234-5678")
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number', 'date_of_birth']

    objects = UserManager()

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자 목록"
        db_table = "user"

    def __str__(self):
        return self.email

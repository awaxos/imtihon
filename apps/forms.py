from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))


# from django.contrib.auth.forms import UserCreationForm
#
# from .models import CustomUser
#
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('email',)
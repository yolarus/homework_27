from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистрации пользователя в интернет-магазине
    """
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        """
        Стилизация формы при инициализации
        """
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Email"
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите пароль"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Повторите пароль"
        })


class LoginUserForm(AuthenticationForm):
    """
    Форма для входа пользователя в интернет-магазин
    """
    def __init__(self, *args, **kwargs):
        """
        Стилизация формы при инициализации
        """
        super(LoginUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Email"
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите пароль"
        })

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm
from .models import User


# Create your views here.
class UserRegisterView(CreateView):
    """
    Класс-представление для регистрации пользователя
    """
    model = User
    template_name = "users/user_form.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

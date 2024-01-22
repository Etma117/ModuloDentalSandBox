


from django.urls import path
from usuarios.views import UserCreateViewDentista

urlpatterns = [
    path('registrar-usuario/', UserCreateViewDentista.as_view(), name='register_user_dentista'),


]
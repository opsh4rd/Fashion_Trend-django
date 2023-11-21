from django.urls import path
from users.views import login, registration, logout_view

urlpatterns = [
    path('login/', login, name='login'),  # логин
    path('registration/', registration, name='registration'),  # регистрация
    path('logout/', logout_view, name='logout'),  # выход

]

from django.urls import path
from users.views import login, registration

urlpatterns = [
    path('login/', login, name='login'),  # login
    path('registration/', registration, name='registration'),  # login

]

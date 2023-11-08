from django.urls import path
from users.views import login, registration, logout_view

urlpatterns = [
    path('login/', login, name='login'),  # login
    path('registration/', registration, name='registration'),  # login
    path('logout/', logout_view, name='logout'),

]

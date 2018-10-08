from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('logout', views.logout),
    path('mainPage', views.main_page)
]

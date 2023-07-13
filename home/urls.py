from . import views
from django.urls import path


urlpatterns = [
    path('',views.home, name="/"),
    path('login', views.login, name="login"),
    path('create_account', views.create_account, name="create_acc"),
    path('logout', views.logout, name="logout")
]
from . import views
from django.urls import path


urlpatterns = [
    path('',views.home, name="/"),
    path('login', views.login, name="login"),
    path('create_account', views.create_account, name="create_acc"),
    path('logout', views.logout, name="logout"),
    path('pricing', views.pricing, name='pricing'),
    path('buy_course/<str:module_code>', views.buy, name='buy_course'),
    path('download', views.downlaod_file, name='download')
]
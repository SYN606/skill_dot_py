from . import views
from django.urls import path


urlpatterns = [
    path('', views.by_us_homepage, name='by_us_homepage')
]

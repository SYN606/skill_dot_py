from . import views
from django.urls import path


urlpatterns = [
    path('', views.nielit_homepage, name='nielit_homepage'),
    path('o_level', views.o_level, name='o_level')
]

from . import views
from django.urls import path


urlpatterns = [
    path('', views.nielit_homepage, name='nielit_homepage'),
    path('<str:course_name>', views.c_details, name='course-detail')
]

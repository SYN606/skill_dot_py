from . import views
from django.urls import path


urlpatterns = [
    path('', views.nielit_homepage, name='nielit_homepage'),
    path('<int:course_id>', views.c_details, name='course-detail')
]

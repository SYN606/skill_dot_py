from django.shortcuts import render
from .models import c_intro



def nielit_homepage(request):
    data = {
        'title' : 'Nielit Courses',
        
            }
    return render(request, 'nielit-index.html', data)

def c_details(request,course_id):
    c_detail = c_intro.objects.filter(id=course_id)
    print(c_detail)
    data = {
        'c_intro' : c_detail
    }
    return render(request, 'c-detail.html', data)
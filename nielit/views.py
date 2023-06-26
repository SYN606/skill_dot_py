from django.shortcuts import render
from .models import c_intro
from .models import Module
from .models import Syllabus

def nielit_homepage(request):
    data = {
        'title' : 'Nielit Courses',
        
            }
    return render(request, 'nielit-index.html', data)

def c_details(request,course_name):
    c_detail = c_intro.objects.filter(c_name=course_name)

    cn_id = 0
    if course_name == "O Level":
        cn_id = 1
    elif  course_name == "CCC":
        cn_id = 2
    
    papers = Module.objects.filter(course_name_id=cn_id)
    

    syllabus = Syllabus.objects.filter()

    
    data = {
        'c_intro' : c_detail,
        'papers' : papers,
        'syllabus' : syllabus
    }
    return render(request, 'c-detail.html', data)
from django.shortcuts import render
from .models import O_level



def nielit_homepage(request):
    c_intro = O_level.objects.all()
    data = {
        'title' : 'Nielit Courses',
        'key' : 'Anubhav Vikram Singh',
    }
    return render(request, 'nielit-index.html', data)

def o_level(request):
    data = {
        'title' : 'O Level'
    }
    return render(request, 'o-level.html', data)
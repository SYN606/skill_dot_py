from django.shortcuts import render

# Create your views here.
def nielit_homepage(request):
    data = {
        'title' : 'Nielit Courses'
    }
    return render(request, 'nielit-index.html', data)

def o_level(request):
    data = {
        'title' : 'O Level'
    }
    return render(request, 'o-level.html', data)
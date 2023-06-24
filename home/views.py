from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'title' : 'Homepage'
    }
    return render(request, 'index.html', data)
from django.shortcuts import render

# Create your views here.

def by_us_homepage(request):
    return render(request, 'by-us-index.html')
from django.shortcuts import render, redirect
from .models import Partner
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout as auth_logout

def home(request):
    
    partners = Partner.objects.all()
    
    data = {
        'title' : 'Homepage',
        'partner' : partners
        
    }
    return render(request, 'index.html', data)


def login(request):
    data = {
        'title' : 'Login'
    }
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(
                                    username = user_name, 
                                    password = password
                                    )
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'user_login.html', data)
    
def logout(request):
    auth_logout(request)
    messages.warning(request, 'Logged out successfully')
    return redirect('/')
    
def create_account(request):
    
    data = {
        'title' : 'Create New User'
    }
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        user_email = request.POST['email']
        password = request.POST['password_1']
        confirm_password = request.POST['password_2']

        if User.objects.filter(username = username).exists():
            messages.warning(request, 'Username is already taken.')
            return render(request, 'create_user.html', data)
            
        
        elif User.objects.filter(email = user_email).exists():
            messages.warning(request, 'Email is already taken.')
            return render(request, 'create_user.html', data)

        else:
            if password == confirm_password:
                
                my_user = User.objects.create_user(username, user_email, password)
                my_user.first_name = first_name
                my_user.last_name = last_name
                
                my_user.save()
                
                messages.success(request, "Your account has been created successfully.")
                
                return redirect('login')

            else:
                messages.warning(request, "Password didn't match")
                
                return render(request, 'create_user.html', data)
    else:
        return render(request, 'create_user.html', data)
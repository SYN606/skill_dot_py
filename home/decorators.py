from django.shortcuts import redirect

def check_authenticated_user(view_function):
    def logic(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)
        
    return logic


def allowed_users(user_allowed = []):
    def deco_func(view_function):
        def logic(request, *args, **kwargs):
            return view_function(request, *args, **kwargs)
        return logic
    return deco_func
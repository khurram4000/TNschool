from django.shortcuts import redirect

def token_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'api_token' not in request.session:
            # Redirect to login page or display error message
            return redirect('login')  # Replace 'login' with your login URL name
        return view_func(request, *args, **kwargs)
    return wrapper

from django.shortcuts import redirect
from functools import wraps

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')  # Redirect to login if user is not authenticated
        return view_func(request, *args, **kwargs)
    return _wrapped_view
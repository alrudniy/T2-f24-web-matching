from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from werkzeug.security import check_password_hash  # Werkzeug for password hashing
from .models import session, User  # Import SQLAlchemy session and User model
from .forms import LoginForm
from .forms import CreateUserForm
from django.contrib.auth import logout # Import logout
from django.contrib.auth.decorators import login_required
from .decorators import custom_login_required  # Import your custom decorator
# import hashlib
from werkzeug.security import check_password_hash, generate_password_hash

import logging
logger = logging.getLogger('django')

def user_list(request):
    users = session.query(User).all()
    user_dicts = [{col.name: getattr(user, col.name) for col in User.__table__.columns} for user in users]
    return render(request, 'user_list.html', {'users': user_dicts})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Fetch the user from the database
            user = session.query(User).filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                # Simulate the login by manually setting the session variable
                request.session['user_id'] = user.id  # Set user id in the session
                request.session['username'] = user.username  # Optionally, set other session data

                messages.success(request, "You have successfully logged in.")
                logger.info('About to redirect to pick_a_path')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@custom_login_required
def home(request):
    return render(request, 'home.html')

#def pick_a_path(request):
#    if 'user_id' not in request.session:
#        return redirect('login')  # Redirect if the user is not in the session
#
#    return render(request, 'pick_a_path.html')

    
@custom_login_required
def scenario1(request):
    return render(request, 'scenario1.html')

@custom_login_required
def scenario2(request):
    return render(request, 'scenario2.html')

@custom_login_required
def article1(request):
    return render(request, 'article1.html')

def logout_view(request):
    logout(request)
    return redirect('login')


import hashlib
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from .models import session, User  # Assuming User is your SQLAlchemy User model

def signup_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Use scrypt for secure password hashing
            password = form.cleaned_data.get('password1')
            hashed_password = generate_password_hash(password, method='scrypt')

            # Create and save the new user with the hashed password
            user = User(
                username=form.cleaned_data.get('username'),
                firstname=form.cleaned_data.get('firstname'),
                lastname=form.cleaned_data.get('lastname'),
                password=hashed_password  # Store the hashed password
            )
            session.add(user)
            session.commit()

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = CreateUserForm()

    return render(request, 'signup.html', {'form': form})

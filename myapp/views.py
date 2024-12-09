from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings  # noqa: F401
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy
import logging
import os

from .decorators import custom_login_required
from .forms import LoginForm, CreateUserForm, PropertyForm
from .models import (
    session, User, Property, PropertyImage, Match
)


logger = logging.getLogger('django')



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Fetch the user from the database
            user = session.query(User).filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                # Simulate the login by setting the session variable
                request.session['user_id'] = user.id
                request.session['username'] = user.username

                messages.success(request, "You have successfully logged in.")
                logger.info('About to redirect to pick_a_path')
                return redirect('pick_a_path')
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@custom_login_required
def pick_a_path(request):
    return render(request, 'pick_a_path.html')



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
                password=hashed_password
            )
            session.add(user)
            session.commit()

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'signup.html', {'form': form})




FEATURES = [
    "Balcony",
    "Multiple floors",
    "Wheelchair access",
    "Pet friendly",
    "Large lot",
    "Low cost",
    "Close to shopping",
    "Close to police station",
    "Close to hospital",
    "Close to fire station",
    "Close to park",
    "Close to school",
    "Close to public transportation",
    "Neighborhood safety",
    "School district quality",
    "Parking availability",
    "Storage space"
]

RATINGS = {}



def index(request):
    return render(request, 'index.html', {'features': FEATURES})




@csrf_exempt
def rate_feature(request, feature):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        RATINGS[feature] = rating
        messages.success(request, f"Rating for {feature} saved successfully!")
        return redirect('index')
    return render(request, 'rate_feature.html', {'feature': feature})




def results(request):
    return render(request, 'results.html', {'ratings': RATINGS})




@custom_login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)  # Handle image upload
        if form.is_valid():
            user_id = request.session.get('user_id')
            if not user_id:
                return redirect('login')  # Redirect to login if not logged in

            property_ = Property(
                name=form.cleaned_data['name'],
                size_sqft=form.cleaned_data['size_sqft'],
                price=form.cleaned_data['price'],
                bedrooms=form.cleaned_data['bedrooms'],
                user_id=user_id,
                street_address=form.cleaned_data['street_address'],
                city=form.cleaned_data['city']
            )
            session.add(property_)
            session.commit()

            image = form.cleaned_data.get('image')
            if image:
                property_image = PropertyImage(
                    property_id=property_.id, image_url=image.name
                )
                session.add(property_image)
                session.commit()

                # Save the uploaded image

                directory = os.path.join(
                    settings.MEDIA_ROOT, 'property_images'
                )
                os.makedirs(directory, exist_ok=True)
                with open(os.path.join(directory, image.name), 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

            messages.success(request, "Property added successfully!")
            return redirect('view_properties')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})



@custom_login_required
def view_properties(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    properties = session.query(Property).filter_by(user_id=user_id).all()
    for property_ in properties:
        property_.images = session.query(PropertyImage).filter_by(
            property_id=property_.id
        ).all()

    return render(request, 'view_properties.html', {
        'properties': properties, 'MEDIA_URL': settings.MEDIA_URL
    })




@custom_login_required
def match_properties(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    property_to_match = session.query(Property).filter(
        Property.user_id != user_id
    ).first()
    if not property_to_match:
        return HttpResponse("No properties available to match.")

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'match':
            match = Match(
                user_id=user_id,
                property_id=property_to_match.id,
                timestamp=sqlalchemy.func.now()
            )
            session.add(match)
            session.commit()


    # Get next property to match, excluding properties the user has already matched
    property_to_match = session.query(Property).filter(
        Property.user_id != user_id,
        ~Property.matches.any(Match.user_id == user_id) # Exclude already matched properties
    ).first()
        if not property_to_match:
            return HttpResponse("No more properties available to match.")

    property_to_match.images = session.query(PropertyImage).filter_by(
        property_id=property_to_match.id
    ).all()

    return render(request, 'match_properties.html', {
        'property': property_to_match, 'MEDIA_URL': settings.MEDIA_URL
    })

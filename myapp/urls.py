from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Root URL (/) for login
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('scenario1/', views.scenario1, name='scenario1'),
    path('scenario2/', views.scenario2, name='scenario2'),
    path('article1/', views.article1, name='article1'),
    path('logout/', views.logout_view, name='logout'),
    path('user_list/', views.user_list, name='userlist'),
]

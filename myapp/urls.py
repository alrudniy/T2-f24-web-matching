from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Root URL (/) for login
    path('signup/', views.signup_view, name='signup'),
    path('pick_a_path/', views.pick_a_path, name='pick_a_path'),
    path('scenario1/', views.scenario1, name='scenario1'),
    path('scenario2/', views.scenario2, name='scenario2'),
    path('article1/', views.article1, name='article1'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),  
    path('', views.movie_page, name='movie_page'),
    path('start/', views.start, name='start'),
    path('submit_credentials/', views.submit_credentials, name='submit_credentials'),
    path('HomePage/', views.home_page, name='home_page'),

]
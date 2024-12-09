from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Root URL (/) for login
    path('signup/', views.signup_view, name='signup'),
    path('pick_a_path/', views.pick_a_path, name='pick_a_path'),
    path('scenario1/', views.scenario1, name='scenario1'),
    path('scenario2/', views.scenario2, name='scenario2'),
    path('article1/', views.article1, name='article1'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('rate/<str:feature>/', views.rate_feature, name='rate_feature'),
    path('results/', views.results, name='results'),
    path('add_property/', views.add_property, name='add_property'),
    path('view_properties/', views.view_properties, name='view_properties'), # New url path
]

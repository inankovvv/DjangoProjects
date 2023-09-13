from django.urls import path
from user_profile import views
from notes_app import views as na_views

app_name = 'user_profile'

urlpatterns = [
    path('', na_views.my_notes),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register')
]


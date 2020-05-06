from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name = 'app-home'),
    path('add/', views.add,name = 'app-add'),
    path('main/', views.main,name = 'app-main'),
    path('signup/', views.signup,name = 'app-signup'),
]
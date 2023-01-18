from django.urls import path

from . import views


urlpatterns = [
    path('' ,  views.home , name="home" ),
    path('register/', views.registerPage , name="register"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.LogoutPage , name="logout"),
    path('update_user/', views.updateUser , name='update_user')
]

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('' ,  views.home , name="home" ),
    path('register/', views.registerPage , name="register"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.LogoutPage , name="logout"),
    path('room/<str:pk>/', views.room , name="room"),
    path('create_room/', views.createRoom , name="create_room"),
    path('update_room/<str:pk>/', views.updateRoom , name="update_room"),
    path('delete_room/<str:pk>/', views.deleteRoom , name="delete_room"),
    path('update_user/', views.updateUser , name="update_user")
]


urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
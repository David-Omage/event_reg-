from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('event/', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('create-event/', views.create_event, name='create-event'),
    path('applauders/', views.applauders, name='applauders'),
    path('seatwarmers/', views.seatwarmers, name='seatwarmers'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
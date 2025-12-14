from django.contrib import admin
from django.urls import path
from pages.views import home, about
from accounts.views import register, profile
from bookings.views import booking_create, booking_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('bookings/', booking_list, name='booking_list'),
    path('bookings/create/', booking_create, name='booking_create'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]

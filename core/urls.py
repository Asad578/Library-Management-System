from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/books/', views.BooksView.as_view(), name='books'),
    path('dashboard/my-bookings/', views.MyBookingsView.as_view(), name='my_bookings'),
    path('dashboard/pendings/', views.PendingsView.as_view(), name='pendings'),
    path('dashboard/approved/', views.ApprovedView.as_view(), name='approved'),
]

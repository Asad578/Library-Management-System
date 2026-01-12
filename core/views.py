from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from .models import User


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'core/home.html'


class AboutView(TemplateView):
    """About page view"""
    template_name = 'core/about.html'


class ContactView(TemplateView):
    """Contact page view"""
    template_name = 'core/contact.html'

    def post(self, request, *args, **kwargs):
        """Handle contact form submission"""
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Here you can add logic to send email or save to database
        # For now, we'll just show a success message
        messages.success(
            request,
            f'Thank you {name}! Your message has been received. We will get back to you soon.'
        )
        return render(request, self.template_name)


@require_http_methods(["GET", "POST"])
def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('core:dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'core/login.html')


@require_http_methods(["GET", "POST"])
def signup_view(request):
    """User signup view"""
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        if not all([username, email, password1, password2]):
            messages.error(request, 'Please fill in all required fields.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                )
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('core:login')
    
    return render(request, 'core/signup.html')


@login_required
def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('core:home')


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    """Dashboard view"""
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class BooksView(TemplateView):
    """Books listing view"""
    template_name = 'core/books.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Add books from database
        context['books'] = []
        return context


@method_decorator(login_required, name='dispatch')
class MyBookingsView(TemplateView):
    """My Bookings view"""
    template_name = 'core/my_bookings.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Add user bookings from database
        context['bookings'] = []
        return context


@method_decorator(login_required, name='dispatch')
class PendingsView(TemplateView):
    """Pending bookings view"""
    template_name = 'core/pendings.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Add pending bookings from database
        context['pendings'] = []
        return context


@method_decorator(login_required, name='dispatch')
class ApprovedView(TemplateView):
    """Approved bookings view"""
    template_name = 'core/approved.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Add approved bookings from database
        context['approved'] = []
        return context

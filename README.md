# Library Management System

A comprehensive Django-based library management system with a clean, modern UI and reusable code structure.

## Features

- **Home Page**: Welcome page with key features overview
- **About Page**: Information about the system and its capabilities
- **Contact Us Page**: Contact form and information
- **Responsive Design**: Modern UI with Bootstrap 5
- **Clean Architecture**: Well-organized, reusable code structure

## Project Structure

```
library-management-system/
├── core/                           # Main application
│   ├── migrations/                  # Database migrations
│   ├── templates/                  # App-specific templates
│   ├── views.py                    # View classes
│   ├── urls.py                     # URL routing
│   └── apps.py                     # App configuration
├── library_management_system/      # Project settings
│   ├── settings/                   # Environment-based settings
│   │   ├── __init__.py            # Environment selector
│   │   ├── base.py                # Common settings
│   │   ├── development.py         # Development settings
│   │   ├── staging.py             # Staging settings
│   │   └── production.py          # Production settings
│   ├── urls.py                     # Main URL configuration
│   ├── wsgi.py                     # WSGI configuration
│   └── asgi.py                     # ASGI configuration
├── templates/                      # Base templates
│   ├── base.html                   # Base template with navbar
│   └── core/                       # App-specific templates
│       ├── home.html
│       ├── about.html
│       ├── contact.html
│       ├── login.html
│       ├── signup.html
│       └── dashboard.html
├── static/                         # Static files
│   └── css/
│       └── style.css               # Custom styles
├── logs/                           # Application logs
├── venv/                           # Virtual environment
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .env                            # Environment variables (not in git)
├── README.md                       # This file
└── ENVIRONMENT_SETUP.md            # Environment setup guide
```

## Setup Instructions

### 1. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` and set your environment:
```bash
DJANGO_ENV=dev  # Options: dev, staging, production
```

**Note:** For production, make sure to:
- Generate a new `SECRET_KEY`
- Set `DEBUG=False`
- Configure database credentials
- Set up email settings

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for detailed environment configuration.

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Or use the existing superuser:
- Username: `admin`
- Password: `admin123`

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## URLs

### Public Pages
- **Home**: `/`
- **About**: `/about/`
- **Contact Us**: `/contact/`
- **Login**: `/login/`
- **Sign Up**: `/signup/`

### Authenticated Pages (Require Login)
- **Dashboard**: `/dashboard/`
- **Books**: `/dashboard/books/`
- **My Bookings**: `/dashboard/my-bookings/`
- **Pendings**: `/dashboard/pendings/`
- **Approved**: `/dashboard/approved/`

### Admin
- **Admin Panel**: `/admin/`

## Code Structure

### Views
- Uses class-based views for better code organization
- `HomeView`, `AboutView`, `ContactView` - Template views
- Contact form handling with POST method

### Templates
- Base template (`base.html`) with reusable navbar and footer
- Bootstrap 5 for responsive design
- Bootstrap Icons for icons
- Custom CSS for enhanced styling

### URLs
- Namespaced URLs using `app_name = 'core'`
- Clean URL patterns
- Easy to extend

## Development

### Adding New Pages

1. Create a new view in `core/views.py`
2. Add URL pattern in `core/urls.py`
3. Create template in `templates/core/`
4. Add navigation link in `templates/base.html`

### Static Files

- Static files are served from `static/` directory
- CSS files in `static/css/`
- Configured in `settings.py` with `STATICFILES_DIRS`

## Technologies Used

- **Django 6.0.1**: Web framework
- **Django REST Framework**: API framework
- **JWT Authentication**: Token-based authentication
- **Bootstrap 5.3.0**: CSS framework
- **Bootstrap Icons 1.11.0**: Icon library
- **python-decouple**: Environment variable management
- **SQLite**: Default database for development (PostgreSQL for production)

## Environment Configuration

This project supports multiple environments:

- **Development**: Debug mode, SQLite, console email
- **Staging**: Production-like settings, PostgreSQL recommended
- **Production**: Full security, PostgreSQL, SMTP email

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for detailed configuration instructions.

## License

This project is open source and available for educational purposes.

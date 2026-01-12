# Environment Setup Guide

This project supports multiple environments: **Development**, **Staging**, and **Production**. Each environment has its own configuration settings.

## Project Structure

```
library_management_system/
├── settings/
│   ├── __init__.py          # Environment selector
│   ├── base.py              # Common settings
│   ├── development.py       # Development settings
│   ├── staging.py           # Staging settings
│   └── production.py        # Production settings
├── .env.example             # Environment variables template
└── .env                     # Your actual environment variables (not in git)
```

## Quick Start

### 1. Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

### 2. Configure Environment

Edit `.env` file and set your environment:

```bash
DJANGO_ENV=dev  # Options: dev, staging, production
```

### 3. Set Required Variables

Update the `.env` file with your actual values, especially:
- `SECRET_KEY` - Generate a new one for production
- Database credentials (if using PostgreSQL)
- Email settings (for production)

## Environment Configuration

### Development Environment

**File:** `settings/development.py`

**Features:**
- Debug mode enabled
- SQLite database (default)
- Console email backend
- Detailed logging to console
- CORS enabled for local development

**Usage:**
```bash
# Set in .env
DJANGO_ENV=dev

# Or set environment variable
export DJANGO_ENV=dev
python manage.py runserver
```

### Staging Environment

**File:** `settings/staging.py`

**Features:**
- Debug mode disabled
- PostgreSQL database (recommended)
- File-based logging
- Security settings enabled (optional SSL)
- SMTP email backend

**Usage:**
```bash
# Set in .env
DJANGO_ENV=staging

# Or set environment variable
export DJANGO_ENV=staging
python manage.py runserver
```

### Production Environment

**File:** `settings/production.py`

**Features:**
- Debug mode disabled (required)
- PostgreSQL database (required)
- Full security settings enabled
- Rotating file logs
- WhiteNoise for static files
- SMTP email backend

**Usage:**
```bash
# Set in .env
DJANGO_ENV=production

# Or set environment variable
export DJANGO_ENV=production
python manage.py collectstatic
gunicorn library_management_system.wsgi:application
```

## Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DJANGO_ENV` | Environment name | `dev`, `staging`, `production` |
| `SECRET_KEY` | Django secret key | Generated key (required in production) |

### Database Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_ENGINE` | Database engine | `django.db.backends.sqlite3` |
| `DB_NAME` | Database name | `db.sqlite3` |
| `DB_USER` | Database user | (empty) |
| `DB_PASSWORD` | Database password | (empty) |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |

### Security Variables (Production)

| Variable | Description | Default |
|----------|-------------|---------|
| `SECURE_SSL_REDIRECT` | Force HTTPS | `True` |
| `SESSION_COOKIE_SECURE` | Secure session cookies | `True` |
| `CSRF_COOKIE_SECURE` | Secure CSRF cookies | `True` |
| `SECURE_HSTS_SECONDS` | HSTS duration | `31536000` |

### Email Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `EMAIL_BACKEND` | Email backend | `console` (dev), `smtp` (prod) |
| `EMAIL_HOST` | SMTP host | `localhost` |
| `EMAIL_PORT` | SMTP port | `587` |
| `EMAIL_USE_TLS` | Use TLS | `True` |
| `EMAIL_HOST_USER` | SMTP username | (empty) |
| `EMAIL_HOST_PASSWORD` | SMTP password | (empty) |

## Generating Secret Key

Generate a new secret key for production:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Database Setup

### SQLite (Development)

No additional setup required. Just set in `.env`:

```bash
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### PostgreSQL (Staging/Production)

1. Install PostgreSQL
2. Create database:

```sql
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
```

3. Update `.env`:

```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=library_db
DB_USER=library_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

4. Run migrations:

```bash
python manage.py migrate
```

## Running the Application

### Development

```bash
# Set environment
export DJANGO_ENV=dev
# Or add to .env: DJANGO_ENV=dev

# Run server
python manage.py runserver
```

### Staging

```bash
# Set environment
export DJANGO_ENV=staging

# Run server
python manage.py runserver
```

### Production

```bash
# Set environment
export DJANGO_ENV=production

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn library_management_system.wsgi:application --bind 0.0.0.0:8000
```

## Environment-Specific Commands

### Development

```bash
DJANGO_ENV=dev python manage.py runserver
DJANGO_ENV=dev python manage.py migrate
DJANGO_ENV=dev python manage.py createsuperuser
```

### Staging

```bash
DJANGO_ENV=staging python manage.py runserver
DJANGO_ENV=staging python manage.py migrate
DJANGO_ENV=staging python manage.py collectstatic
```

### Production

```bash
DJANGO_ENV=production python manage.py migrate
DJANGO_ENV=production python manage.py collectstatic --noinput
DJANGO_ENV=production gunicorn library_management_system.wsgi:application
```

## Logging

### Development
- Logs to console
- Level: DEBUG

### Staging
- Logs to `logs/staging.log`
- Also logs to console
- Level: INFO

### Production
- Logs to `logs/production.log`
- Errors to `logs/errors.log`
- Rotating logs (10MB, 10 backups)
- Level: INFO

## Security Checklist

### Development
- ✅ Debug mode enabled
- ✅ SQLite database
- ✅ Console email

### Staging
- ✅ Debug mode disabled
- ✅ PostgreSQL database
- ✅ File logging
- ⚠️ SSL optional

### Production
- ✅ Debug mode disabled
- ✅ PostgreSQL database
- ✅ SSL/HTTPS enforced
- ✅ Secure cookies
- ✅ HSTS enabled
- ✅ File logging with rotation
- ✅ WhiteNoise for static files

## Troubleshooting

### Settings Not Loading

Make sure `DJANGO_ENV` is set correctly:

```bash
echo $DJANGO_ENV  # Should show: dev, staging, or production
```

### Database Connection Error

Check your database credentials in `.env`:

```bash
# Test PostgreSQL connection
psql -h localhost -U library_user -d library_db
```

### Secret Key Error

Generate a new secret key and update `.env`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Best Practices

1. **Never commit `.env` files** - They contain sensitive information
2. **Use different secret keys** for each environment
3. **Use strong passwords** for production databases
4. **Enable all security settings** in production
5. **Use environment variables** instead of hardcoding values
6. **Test in staging** before deploying to production
7. **Monitor logs** regularly in production

## Additional Resources

- [Django Settings Documentation](https://docs.djangoproject.com/en/stable/topics/settings/)
- [python-decouple Documentation](https://github.com/henriquebastos/python-decouple)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

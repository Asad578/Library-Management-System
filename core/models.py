from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=150)
    edition = models.CharField(max_length=50)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='books'
    )

    authors = models.ManyToManyField(
        Author,
        related_name='books'
    )

    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Issue(models.Model):
    STATUS_CHOICES = (
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='issues'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='issues'
    )

    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='issued'
    )

    def __str__(self):
        return f"{self.book.title} → {self.user.username}"

class Reservation(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    reservation_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    def __str__(self):
        return f"{self.book.title} reserved by {self.user.username}"

class Fine(models.Model):
    issue = models.OneToOneField(
        Issue,
        on_delete=models.CASCADE,
        related_name='fine'
    )

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Fine: {self.amount} ({self.issue.book.title})"

class IssueHistory(models.Model):
    ACTION_CHOICES = (
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('renewed', 'Renewed'),
        ('overdue', 'Overdue'),
        ('fine_paid', 'Fine Paid'),
    )

    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='history'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    action_date = models.DateTimeField(auto_now_add=True)

    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} - {self.action}"


from django.contrib import admin
from .models import User, Category, Author, Book, Issue, Reservation, Fine, IssueHistory

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role', {'fields': ('role',)}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'category', 'publisher', 'total_copies', 'available_copies', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'isbn', 'publisher')
    filter_horizontal = ('authors',)
    readonly_fields = ('created_at',)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'issue_date', 'due_date', 'status')
    list_filter = ('status', 'issue_date', 'due_date')
    search_fields = ('book__title', 'user__username')
    readonly_fields = ('issue_date',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'reservation_date', 'status')
    list_filter = ('status', 'reservation_date')
    search_fields = ('book__title', 'user__username')
    readonly_fields = ('reservation_date',)

@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('id', 'issue', 'amount', 'is_paid', 'paid_date')
    list_filter = ('is_paid',)
    search_fields = ('issue__book__title', 'issue__user__username')
    readonly_fields = ('issue',)

@admin.register(IssueHistory)
class IssueHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'issue', 'user', 'action', 'action_date')
    list_filter = ('action', 'action_date')
    search_fields = ('book__title', 'user__username', 'action')
    readonly_fields = ('action_date',)

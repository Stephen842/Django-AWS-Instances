from django.contrib import admin
from .models import MyUser, EC2Instance
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class MyUserAdmin(UserAdmin):
    model = MyUser
    form = UserChangeForm  # Use UserChangeForm for managing users

    # Specify the fields to be displayed in the list view
    list_display = ('id', 'name', 'username', 'email', 'is_active', 'is_staff')

    # Add filters in the right sidebar
    list_filter = ('is_active', 'is_staff')

    # Add a search bar at the top of the list view
    search_fields = ('name', 'username', 'email', 'phone',)

    # Add fields to be displayed in the detail view
    fieldsets = (
        (None, {'fields': ('name', 'username', 'email', 'phone', 'password', 'is_active', 'is_staff')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )

class EC2InstanceAdmin(admin.ModelAdmin):
    list_display = ('instance_id', 'state')

    search_fields = ('user', 'instance_id', 'instance_type', 'state',)

    fieldsets = [
        (None, {'fields': ('user', 'instance_id', 'instance_type', 'state', 'ip_address', 'created_at', 'updated_at')})
    ]

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(EC2Instance, EC2InstanceAdmin)
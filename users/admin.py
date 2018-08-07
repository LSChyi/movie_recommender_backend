from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Rating

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [ 'email', 'id', 'training_id' ]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Rating)

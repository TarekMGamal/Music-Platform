from django.contrib import admin
from .models import User

@admin.register(User)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('USERNAME_FIELD', 'EMAIL_FIELD',)
    
    
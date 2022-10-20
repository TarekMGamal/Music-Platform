from django.contrib import admin
from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_datetime',)
    
    fieldsets = (
        (None, { "fields": ('name',) }),
        (None, { "fields": ('artist',) }),
        (None, { "fields": ('release_datetime',) }),
        (None, { "fields": ('creation_datetime',) }),
        (None, { "fields": ('cost',) }),
        (None, {
            "fields": ('is_approved',),
            "description": 'Approve the album if its name is not explicit'
        })
    )
    
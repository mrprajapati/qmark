from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject',
                    'sent_at',)
    search_fields = ('name', 'email',)
    list_filter = ('sent_at',)


admin.site.register(Contact, ContactAdmin)

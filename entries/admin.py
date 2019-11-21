from django.contrib import admin
from .models import Entry,Category,Tag
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ['entry_title', 'entry_date', 'category', 'entry_author']
    fields = ['entry_title', 'entry_text', 'entry_excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.entry_author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Entry,EntryAdmin)
admin.site.register(Category)
admin.site.register(Tag)
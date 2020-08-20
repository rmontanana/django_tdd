from django.contrib import admin
from .models import Entry, Comment

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

@admin.register(Comment)
class CommentAdim(admin.ModelAdmin):
    pass
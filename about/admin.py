from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content', 'updated_on')
    search_fields = ['title', 'content', 'updated_on']
    list_filter = ('title', 'updated_on',)
    
    summernote_fields = ('content',)
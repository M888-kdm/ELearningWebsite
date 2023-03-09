from dataclasses import Field
from django.contrib import admin
from .models import Subject, Course, Module, Content, Text, File, Image, Video
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepolutated_fields = {'slug': ('title',)}
    
    
class ModuleInline(admin.StackedInline):
    model = Module
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    
admin.site.index_template = 'memcache_status/admin_index.html'

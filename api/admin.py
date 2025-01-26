from django.contrib import admin
from .models import Category, Picture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('category', 'caption', 'uploaded_at')
    search_fields = ('caption', 'category__name')
    list_filter = ('category',)
    ordering = ('-uploaded_at',)
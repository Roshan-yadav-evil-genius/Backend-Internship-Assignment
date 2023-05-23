from django.contrib import admin
from .models import Category,Subcategory,Event
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=["event_type","name","user","rigor_rank"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["name"]

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=["category","name"]
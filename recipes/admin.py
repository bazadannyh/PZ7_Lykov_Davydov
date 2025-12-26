from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'cooking_time', 'difficulty', 'created_at')
    list_filter = ('difficulty', 'created_at')
    search_fields = ('title', 'description', 'ingredients')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'image')
        }),
        ('Детали рецепта', {
            'fields': ('ingredients', 'cooking_time', 'difficulty')
        }),
        ('Дополнительно', {
            'fields': ('created_at', 'updated_at')
        }),
    )
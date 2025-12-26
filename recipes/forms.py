from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 
            'description', 
            'ingredients',
            'cooking_time', 
            'difficulty', 
            'image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название рецепта'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Опишите процесс приготовления'
            }),
            'ingredients': forms.Textarea(attrs={
                'rows': 6,
                'class': 'form-control',
                'placeholder': 'Каждый ингредиент с новой строки'
            }),
            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
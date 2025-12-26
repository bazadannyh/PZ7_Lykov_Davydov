from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name="Название рецепта"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    ingredients = models.TextField(
        verbose_name="Ингредиенты",
        help_text="Каждый ингредиент с новой строки"
    )
    cooking_time = models.IntegerField(
        verbose_name="Время приготовления (минуты)"
    )
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ('легко', 'Легко'),
            ('средне', 'Средне'),
            ('сложно', 'Сложно'),
        ],
        default='средне',
        verbose_name="Сложность"
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ['-created_at']
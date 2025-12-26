from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 10

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'id': recipe.id,
                    'title': recipe.title,
                    'cooking_time': recipe.cooking_time,
                    'difficulty': recipe.get_difficulty_display(),
                })
            return redirect('recipe_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                }, status=400)
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('recipe_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                }, status=400)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/recipe_form.html', {
        'form': form,
        'recipe': recipe,
        'update': True
    })

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        recipe.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return redirect('recipe_list')
    
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
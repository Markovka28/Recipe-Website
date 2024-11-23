from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Установка автора как текущего пользователя
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
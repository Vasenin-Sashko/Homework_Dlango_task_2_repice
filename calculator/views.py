
from multiprocessing import context
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salad': {
        'огурец, шт': 1,
        'помдор, шт': 2,
        'зелень, г': 10,
        'сметана, г': 50,
    },
    # можете добавить свои рецепты ;)
}

def recipe_food(request, recipe_name):
    servings = request.GET.get('servings', 1)
    if recipe_name in DATA:
        recipe = DATA[recipe_name]
        result = dict()
        for key, value in recipe.items():
            new_value = value * int(servings)
            result[key] = new_value
        
        context = {
            'recipe_name': recipe,
            'recipe': result
        }
        return render(request, 'calculator/index.html', context)
    
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

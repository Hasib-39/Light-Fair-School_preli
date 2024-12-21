# urls.py
from django.urls import path

from .views import (ChatbotQueryView, RecipeRecommendationView, RecipeView,
                    add_ingredient, delete_ingredient_by_id,
                    get_ingredient_by_name, update_ingredient_by_id)

urlpatterns = [
    path('ingredients/add/', add_ingredient, name='add_ingredient'),
    path('ingredients/update/<int:id>/', update_ingredient_by_id, name='update_ingredient'),
    path('ingredients/delete/<int:id>/', delete_ingredient_by_id, name='delete_ingredient'),
    path('ingredients/', get_ingredient_by_name, name='get_ingredient_by_name'),
    path('recipes/add', RecipeView.as_view(), name='add_recipe'),
    path('recipes/recommend', RecipeRecommendationView.as_view(), name='recipe_recommend'),
    path('chatbot/query', ChatbotQueryView.as_view(), name='chatbot_query'),
]

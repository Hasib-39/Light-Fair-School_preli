# views.py
import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ingredient, Recipe
from .serializers import IngredientSerializer


@api_view(['POST'])
def add_ingredient(request):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_ingredient_by_name(request):
    # Retrieve the ingredient name from query parameters
    name = request.query_params.get('name', None)

    if name is None:
        return Response({"detail": "Ingredient name is required."}, status=status.HTTP_400_BAD_REQUEST)

    # Filter ingredients by the provided name (case-insensitive search)
    ingredients = Ingredient.objects.filter(name__icontains=name)

    if not ingredients.exists():
        return Response({"detail": "No ingredients found with the given name."}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the filtered ingredients and return the response
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_ingredient_by_id(request, id):
    try:
        name = Ingredient.objects.get(pk=id)
    except Ingredient.DoesNotExist:
        return Response({"detail": "Ingredient not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = IngredientSerializer(name, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_ingredient_by_id(request, id):
    try:
        ingredient = Ingredient.objects.get(pk=id)
    except Ingredient.DoesNotExist:
        return Response({"detail": "Ingredient not found."}, status=status.HTTP_404_NOT_FOUND)

    ingredient.delete()
    return Response({"detail": "Ingredient deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class RecipeView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        recipe = Recipe.objects.create(
            name=data['recipe_name'],
            instructions=data['instructions'],
            taste=data['taste'],
            reviews=data['reviews'],
            cuisine=data['cuisine'],
            preparation_time=data['preparation_time']
        )
        for ingredient_name in data['ingredients']:
            ingredient = Ingredient.objects.get(name=ingredient_name)
            recipe.ingredients.add(ingredient)
        return JsonResponse({"message": "Recipe added successfully", "recipe": {
            "id": recipe.id,
            "recipe_name": recipe.name,
            "ingredients": [ingredient.name for ingredient in recipe.ingredients.all()],
            "instructions": recipe.instructions,
            "taste": recipe.taste,
            "reviews": recipe.reviews,
            "cuisine": recipe.cuisine,
            "preparation_time": recipe.preparation_time
        }})


class RecipeRecommendationView(View):
    def get(self, request):
        ingredients = request.GET.get('ingredients').split(',')
        recipes = Recipe.objects.filter(ingredients__name__in=ingredients)
        recipe_list = [{
            "recipe_name": recipe.name,
            "ingredients": [ingredient.name for ingredient in recipe.ingredients.all()],
            "instructions": recipe.instructions,
            "taste": recipe.taste,
            "reviews": recipe.reviews,
            "cuisine": recipe.cuisine,
            "preparation_time": recipe.preparation_time
        } for recipe in recipes]
        return JsonResponse({"message": "Recipes found", "recipes": recipe_list})


class ChatbotQueryView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        # Here you would integrate the LLM model for recipe suggestion
        query = data['user_query']
        # For now, we're using a simple placeholder logic
        recipes = Recipe.objects.filter(taste__icontains="sweet")
        recipe_list = [{
            "recipe_name": recipe.name,
            "ingredients": [ingredient.name for ingredient in recipe.ingredients.all()],
            "instructions": recipe.instructions,
            "taste": recipe.taste,
            "reviews": recipe.reviews,
            "cuisine": recipe.cuisine,
            "preparation_time": recipe.preparation_time
        } for recipe in recipes]
        return JsonResponse({"message": "Here are some sweet recipes based on your preferences", "recipes": recipe_list})

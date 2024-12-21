from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True, null=True)  # e.g., "2 cups", "500g"
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()  # Store as comma-separated values
    instructions = models.TextField()
    taste = models.CharField(max_length=50, choices=[("sweet", "Sweet"), ("spicy", "Spicy"), ("sour", "Sour")])
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)
    preparation_time = models.PositiveIntegerField(help_text="Time in minutes")
    reviews = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

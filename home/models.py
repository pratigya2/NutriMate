from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length = 100)
    image = models.FileField()
    ingredients = models.TextField()
    meal_link = models.TextField()
    recipe = models.TextField()
    is_snack = models.BooleanField(null= False,default=False)
    is_lunch = models.BooleanField(null = False,default=False)
    is_dinner= models.BooleanField(null = False,default=False)
    is_breakfast = models.BooleanField(null=False,default=False)
    is_confection = models.BooleanField(null = False,default=False)

    def __str__(self):
        return self.name
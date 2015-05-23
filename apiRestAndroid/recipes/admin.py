from django.contrib import admin

from .models import Recipe



class RecipeAdmin(admin.ModelAdmin):    
    list_display = ('name', 'ingredients', 'recipe_type', 'time', 'chef_name')
    list_filter = ('name', 'chef_name' , 'recipe_type')
    search_fields = ('name', 'recipe_type' , 'chef_name')
    list_editable = (  'recipe_type', 'time', 'chef_name')

admin.site.register(Recipe , RecipeAdmin)    
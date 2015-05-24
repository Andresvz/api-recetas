from django.shortcuts import render

import django_filters
from .models import Recipe
from rest_framework import viewsets, serializers
from rest_framework import filters
from rest_framework import generics

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ['name','chef_name']

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe


class RecipeViewSet(viewsets.ModelViewSet):
	 queryset = Recipe.objects.all()
	 serializer_class = RecipeSerializer
	 filter_class = RecipeFilter


	
	
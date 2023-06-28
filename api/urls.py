from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('add/condition/', views.addCondition),
    # path('add/goal/', views.addGoal),
    path('conditions/', views.getConditions),
    path('nutritional-advice/', views.getNutritionalAdvice)
]
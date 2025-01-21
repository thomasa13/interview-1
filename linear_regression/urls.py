from django.urls import path
from . import views

urlpatterns = [
    path('linear_regression/', views.homepage, name="homepage"),
    path('api/linear_regression/', views.api_likelihood_by_age, name="api"),
]
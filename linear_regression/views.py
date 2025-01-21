from django.shortcuts import render
from linear_regression.models import BeerDrinkers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def homepage(request):
    if 'age' in request.GET :
        likelihood_of_liking_beer, r2 = BeerDrinkers.get_likelihood_by_age(int(request.GET['age']))
        return render(request, "homepage.html", { 
            "age": request.GET['age'],
            "likelihood_of_liking_beer": likelihood_of_liking_beer * 100, 
            "r2": r2 * 100,
        })
    else:
        return render(request, "homepage.html", { 
            "age": None,
            "likelihood_of_liking_beer": None,
            "r2": None,
        })
    
@api_view(['POST'])
def api_likelihood_by_age(request):
    age = request.data.get('age')
    if not isinstance(age, int):
        return Response('Property "age" is missing or invalid, must be of type int.', status=status.HTTP_200_OK)
    
    likelihood_of_liking_beer, r2 = BeerDrinkers.get_likelihood_by_age(age)
    return Response({
        "likelihood_of_liking_beer": likelihood_of_liking_beer, 
        "r2": r2,
    })
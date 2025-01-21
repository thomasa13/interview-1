from django.db import models
from django.db.models import Avg, Case, When, FloatField

class BeerDrinkers(models.Model):
  age = models.IntegerField()
  likes_beer = models.BooleanField()

  staticmethod
  def get_likelihood_by_age(age: int):
    from sklearn.linear_model import LinearRegression

    likelihood_per_age = (
        BeerDrinkers.objects
        .values('age')
        .annotate(
            likelihood=Avg(
                Case(
                    When(likes_beer=True, then=1.0),
                    default=0.0,
                    output_field=FloatField(),
                )
            )
        )
    )
    x = [[x['age']] for x in likelihood_per_age]
    y =[x['likelihood'] for x in likelihood_per_age]
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(x, y)

    return linear_regression_model.predict([[age]])[0], linear_regression_model.score(x, y)
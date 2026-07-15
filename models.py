from django.db import models

# Create your models here.
class HDIRecord(models.Model):
    country = models.CharField(max_length=100)
    life_expectancy = models.FloatField()
    mean_years_schooling = models.FloatField()
    expected_years_schooling = models.FloatField()
    gni_per_capita = models.FloatField()
    hdi_category = models.CharField(max_length=20)

    def __str__(self):
        return self.country


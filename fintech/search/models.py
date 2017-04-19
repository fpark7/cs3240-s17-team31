from django.db import models

# Create your models here.

class Search(models.Model):

    COUNTRIES = (('US', 'United States'),
                 ('CA', 'Canada'),
                 ('GB', 'Great Britain'),
                 ('MX', 'Mexico'),)

    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'),)

    # owner = models.CharField(required=False, max_length=50)
    match = models.CharField(max_length=1, choices=OPTIONS)
    is_private = models.CharField(max_length=1, choices=OPTIONS)
    company_name = models.CharField(max_length=45)
    company_Phone = models.CharField(max_length=11)
    company_location = models.CharField(max_length=45)
    company_country = models.CharField(max_length=2, choices=COUNTRIES)
    sector = models.CharField(max_length=45)
    projects = models.CharField(max_length=30)

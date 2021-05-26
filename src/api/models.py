from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.utils.translation import gettext_lazy as _

class ZillowEstimate(models.Model):
 
   zillow_id = models.PositiveIntegerField(null=True)
   rentzestimate_amount = models.PositiveIntegerField(null=True)
   rentzestimate_last_updated = models.DateField(null=True)
   zestimate_amount = models.PositiveIntegerField(null=True)
   zestimate_last_updated = models.DateField(null=True)


class Listing(models.Model):
 
   area_unit = models.CharField(max_length=10, default="SqFt")
   bathrooms = models.FloatField(null=True)
   bedrooms = models.PositiveSmallIntegerField(null=True) # could also have choices
   home_size = models.PositiveIntegerField(null=True)
   class HomeType(models.TextChoices):
       SINGLEFAMILY = 'SingleFamily', _('Single Family')
       CONDOMINIUM = 'Condominium', _('Condominium')
       MULTIFAMILY = 'MultiFamily2to4', _('Multi-Family (2 to 4)')
       VACANT = 'VacantResidentialLand', _('Vacant Residential Land')
       APARTMENT = 'Apartment', _('Apartment')
 
   home_type = models.CharField(
       max_length=22,
       choices=HomeType.choices,
       default=HomeType.SINGLEFAMILY
   )
   last_sold_date = models.DateField(null=True)
   last_sold_price = models.PositiveIntegerField(null=True)
   link = models.URLField(null=True)
   price = models.CharField(max_length=7, default="")
   property_size = PositiveIntegerField(null=True)
   rent_price = PositiveIntegerField(null=True)
   zillow_details = models.ForeignKey(
       ZillowEstimate,
       on_delete=models.CASCADE,
       related_name="listing",
       null=True)
   tax_value = models.FloatField(null=True)
   tax_year = models.CharField(max_length=4, default="")
   year_built = models.CharField(max_length=4, default="")
   address = models.CharField(max_length=80)
   city = models.CharField(max_length=40) # could have choices
   state = models.CharField(max_length=2) # should have choices (CA -> California) etc.
   zipcode = models.CharField(max_length=5)
 
 
   def __str__(self):
       return f"{self.__class__.__name__}(home_type:{self.home_type}, price:{self.price})"
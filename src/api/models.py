from django.db import models
from django.db.models.fields import PositiveIntegerField

class ZillowEstimate(models.Model):
 
   zillow_id = models.PositiveIntegerField(null=True)
   rentzestimate_amount = models.PositiveIntegerField(null=True)
   rentzestimate_last_updated = models.DateField(null=True)
   zestimate_amount = models.PositiveIntegerField(null=True)
   zestimate_last_updated = models.DateField(null=True)

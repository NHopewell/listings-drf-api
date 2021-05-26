from rest_framework import serializers

from .models import ZillowEstimate

class ZillowEstimateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ZillowEstimate
        fields = (
               "zillow_id", "rentzestimate_amount", "rentzestimate_last_updated",
               "zestimate_amount", "zestimate_last_updated",
        )
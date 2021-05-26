from rest_framework import serializers

from .models import ZillowEstimate, Listing

class ZillowEstimateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ZillowEstimate
        fields = (
               "zillow_id", "rentzestimate_amount", "rentzestimate_last_updated",
               "zestimate_amount", "zestimate_last_updated",
        )

class ListingSerializer(serializers.ModelSerializer):

    zillow_details = ZillowEstimateSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = (
            "id", "area_unit", "bathrooms", "bedrooms", "home_size",
            "home_type", "last_sold_date", "last_sold_price",
            "link", "price", "property_size", "rent_price",
            "zillow_details", "tax_value", "tax_year",
            "year_built", "address", "city", "state", "zipcode",)
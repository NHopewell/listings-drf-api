from django.shortcuts import render

from api.models import Listing
from api.serializers import ListingSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny



"""
# using generic views if we want to be less verbose

from rest_framework import generics


class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerialier
"""


class ListingList(APIView):
    """
    List all listings, or create a new listing.
    """
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        """list all listings view. TODO: paginate results"""
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """create listing view."""
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingDetail(APIView):
    """
    Retrieve, update or delete a listing.
    """
    permission_classes = (AllowAny, )
    
    def get_object(self, listing_id):
        """get a listing instance"""
        try:
            return Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, listing_id, *args, **kwargs):
        """get listing with id"""
        listing = self.get_object(listing_id)
        serializer = ListingSerializer(listing)

        return Response(serializer.data)

    def put(self, request, listing_id, *args, **kwargs):
        """update listing with id"""
        listing = self.get_object(listing_id)
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, listing_id, *args, **kwargs):
        """delete listing with id"""
        listing= self.get_object(listing_id)
        listing.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

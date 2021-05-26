from django.shortcuts import render

from api.models import Listing
from api.serializers import ListingSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



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
    def get(self, request, *args, **kwargs):
        """list all listings view. TODO: paginate results"""
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """create listing view. TODO: paginate"""
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


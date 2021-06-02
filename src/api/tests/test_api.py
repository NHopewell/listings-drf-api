import json

from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status

from api.models import Listing


class TestListingListView(TestCase):
    """
    Test casts for api.ListingListView ( "listings-list" )

    tests:
        -a valid put request
        -an invalid put request
        -a get request
    """


    @classmethod
    def setUpTestData(cls):


        cls.valid_post_payload = json.dumps({
            "address": "test address updated",
            "city": "test city updated",
            "state": "XX",
            "zipcode": "XXXXX"
        })

        cls.invalid_post_payload = json.dumps({
            "address": "test address updated",
            "city": "test city updated",
            "state": "XX",
        })


    def setUp(self):
        pass


    def test_listing_created(self):
        response = self.client.post(
            reverse("listing-list"),
            data = TestListingListView.valid_post_payload ,
            content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_invalid_listing(self):
        response = self.client.post(
            reverse("listing-list"),
            data = TestListingListView.invalid_post_payload ,
            content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_listing_list(self):
        response = self.client.get(reverse("listing-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def tearDown(self):
        pass



class TestListingDetailView(TestCase):
    """
    Test casts for api.ListingDetailView ( "listings-detail" )

    tests:
        -a get request with listing_id:1
        -a valid put request
        -an invalid put request
        -a get request to listings
        -a delete request with listing_id:1
    """


    @classmethod
    def setUpTestData(cls):
        
        Listing.objects.create(
            address="test address",
            city="test city",
            state="XX",
            zipcode="XXXXX"
        )

        cls.valid_update_payload = json.dumps({
            "address": "test address updated",
            "city": "test city updated",
            "state": "XX",
            "zipcode": "XXXXX"
        })

        cls.invalid_update_payload = json.dumps({
            "address": "test address updated",
            "city": "test city updated",
            "state": "XX",
        })

    
    def setUp(self):
        pass


    def test_get_listing(self):
        response = self.client.get(
            reverse("listing-detail", kwargs={'listing_id': 1}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_listing(self):
        response = self.client.put(
            reverse("listing-detail", kwargs={'listing_id': 1}),
            data = TestListingDetailView.valid_update_payload,
            content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_bad_update(self):
        response = self.client.put(
            reverse("listing-detail", kwargs={'listing_id': 1}),
            data = TestListingDetailView.invalid_update_payload,
            content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_delete_listing(self):
        response = self.client.delete(
            reverse("listing-detail", kwargs={'listing_id': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def tearDown(self):
        pass
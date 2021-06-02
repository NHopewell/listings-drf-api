from django.test import TestCase

from api.models import ZillowEstimate, Listing


class TestListingModel(TestCase):
    """
    Test cases for api.Listing model

    tests:
        -adding a ZillowEstimate nested object to a listing
        -returning the correct complete address from a listing
    """

    @classmethod
    def setUpTestData(cls):
        Listing.objects.create(
            address="test address",
            city="test city",
            state="XX",
            zipcode="XXXXX"
        )


    def setUp(self):
        self.listing = Listing.objects.get(address="test address")


    def test_add_zillow_details(self):
        zdetails = ZillowEstimate.objects.create(
                zillow_id = 9999999,
                rentzestimate_amount = 2900,
                rentzestimate_last_updated = "2018-08-07",
                zestimate_amount = 800000,
                zestimate_last_updated = "2018-08-07"
        )

        self.listing.zillow_details = zdetails

        self.assertTrue(isinstance(self.listing.zillow_details, ZillowEstimate))


    def test_complete_address(self):
        complete_address = self.listing.complete_address

        self.assertEqual(complete_address, "test address, test city, XX, XXXXX")


    def tearDown(self):
        pass

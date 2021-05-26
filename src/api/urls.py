from django.urls import path

from api import views

urlpatterns = [
    path('v1/listings/', views.ListingList.as_view(), name="listing-list"),
    path('v1/listings/<int:listing_id>/', views.ListingDetail.as_view(), name="listing-detail")
]

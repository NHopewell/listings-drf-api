from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]


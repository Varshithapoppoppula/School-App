from django.urls import path
from finance.views import feeCollection
from finance.views import feeCollectionReport
from finance.views import feeDuesReport


urlpatterns = [
    path('feecoll/', feeCollection),
    path('feecollectionreport/', feeCollectionReport),
    path('feedues/', feeDuesReport),
]

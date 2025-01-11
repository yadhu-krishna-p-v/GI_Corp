from django.urls import path
from .views import CsvUploadView

urlpatterns = [
    path('validate-csv/', CsvUploadView.as_view(), name='validate_csv'),
]

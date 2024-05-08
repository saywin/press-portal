from django.urls import path

from redact_radar.views import (
    IndexView,
    NewspaperList,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/", NewspaperList.as_view(), name="newspaper-list")
]

app_name = "redact_radar"

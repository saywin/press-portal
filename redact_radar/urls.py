from django.urls import path

from redact_radar.views import (
    IndexView,
    NewspaperList,
    TopicList,
    RedactorList,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/", NewspaperList.as_view(), name="newspaper-list"),
    path("topic/", TopicList.as_view(), name="topic-list"),
    path("redactor/", RedactorList.as_view(), name="redactor-list"),
]

app_name = "redact_radar"

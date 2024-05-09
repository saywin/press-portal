from django.urls import path

from redact_radar.views import (
    IndexView,
    NewspaperListView,
    TopicListView,
    RedactorListView,
    NewspaperDetailView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/", NewspaperListView.as_view(), name="newspaper-list"),
    path("topic/", TopicListView.as_view(), name="topic-list"),
    path("redactor/", RedactorListView.as_view(), name="redactor-list"),
    path("newspaper/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail")
]

app_name = "redact_radar"

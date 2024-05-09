from django.urls import path

from redact_radar.views import (
    IndexView,
    NewspaperListView,
    TopicListView,
    RedactorListView,
    NewspaperDetailView,
    TopicDetailView,
    RedactorDetailView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspaper/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("topic/", TopicListView.as_view(), name="topic-list"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("redactor/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),

]

app_name = "redact_radar"

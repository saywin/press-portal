from django.urls import path

from redact_radar.views import (
    IndexView,
    NewspaperListView,
    TopicListView,
    RedactorListView,
    NewspaperDetailView,
    TopicDetailView,
    RedactorDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspaper/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspaper/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspaper/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspaper/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("topic/", TopicListView.as_view(), name="topic-list"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("redactor/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),

]

app_name = "redact_radar"

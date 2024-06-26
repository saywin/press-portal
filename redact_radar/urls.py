from django.urls import path

from redact_radar.views import (
    IndexView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    TopicListView,
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "newspaper/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspaper/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspaper/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspaper/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspaper/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "topic/",
        TopicListView.as_view(),
        name="topic-list"
    ),
    path(
        "topic/<int:pk>/",
        TopicDetailView.as_view(),
        name="topic-detail"
    ),
    path(
        "topic/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "topic/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topic/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "redactor/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactor/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactor/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactor/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
]

app_name = "redact_radar"

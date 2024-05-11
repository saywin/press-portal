from django.urls import reverse_lazy
from django.views import generic

from redact_radar.models import Newspaper, Topic, Redactor


class IndexView(generic.ListView):
    template_name = "redact_radar/index.html"
    context_object_name = "context"

    def get_queryset(self):
        return {
            "num_newspapers": Newspaper.objects.count(),
            "num_topics": Topic.objects.count(),
            "num_redactors": Redactor.objects.count(),
        }


class NewspaperListView(generic.ListView):
    model = Newspaper
    template_name = "redact_radar/newspaper_list.html"
    context_object_name = "newspaper_list"
    paginate_by = 3


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    template_name = "redact_radar/newspaper_form.html"
    success_url = reverse_lazy("redact_radar:newspaper_list")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    template_name = "redact_radar/newspaper_form.html"
    success_url = reverse_lazy("redact_radar:newspaper_list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("redact_radar:newspaper_list")
    template_name = "redact_radar/newspaper_confirm_delete.html"


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class TopicListView(generic.ListView):
    model = Topic
    template_name = "redact_radar/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 4
    queryset = Topic.objects.prefetch_related("newspapers")


class TopicDetailView(generic.DetailView):
    model = Topic
    queryset = Topic.objects.prefetch_related("newspapers")


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "redact_radar/topic_form.html"
    success_url = reverse_lazy("redact_radar:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "redact_radar/topic_form.html"
    success_url = reverse_lazy("redact_radar:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("redact_radar:topic-list")
    template_name = "redact_radar/topic_confirm_delete.html"


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "redact_radar/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 3


class RedactorDetailView(generic.DetailView):
    model = Redactor

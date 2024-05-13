from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from redact_radar.forms import (
    RedactorCreateForm,
    RedactorUpdateForm,
    NewspaperCreateForm,
    NewspaperSearchForm,
    NewspaperUpdateForm,
)
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)
        if form.is_valid():
            return self.model.objects.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return self.queryset


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperCreateForm
    template_name = "redact_radar/newspaper_form.html"
    success_url = reverse_lazy("redact_radar:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperUpdateForm
    template_name = "redact_radar/newspaper_form.html"
    success_url = reverse_lazy("redact_radar:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("redact_radar:newspaper-list")
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


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "redact_radar/topic_form.html"
    success_url = reverse_lazy("redact_radar:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "redact_radar/topic_form.html"
    success_url = reverse_lazy("redact_radar:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("redact_radar:topic-list")
    template_name = "redact_radar/topic_confirm_delete.html"


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "redact_radar/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 3


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    template_name = "redact_radar/redactor_form.html"
    success_url = reverse_lazy("redact_radar:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    template_name = "redact_radar/redactor_form.html"
    success_url = reverse_lazy("redact_radar:redactor-list")

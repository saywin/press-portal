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


class NewspaperList(generic.ListView):
    model = Newspaper
    template_name = "redact_radar/newspaper_list.html"
    context_object_name = "newspaper_list"
    paginate_by = 3


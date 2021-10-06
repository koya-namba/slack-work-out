from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import CreateLogForm
from .models import WorkOut


class CreateLogView(CreateView):
    """筋トレlogを作成するView"""

    model = WorkOut
    template_name = 'slack_work_out/create_log.html'
    form_class = CreateLogForm
    success_url = reverse_lazy('slack_work_out:done_log')

    def form_valid(self, form):
        return super(CreateLogView, self).form_valid(form)


class DoneLogView(TemplateView):
    template_name = 'slack_work_out/done_log.html'

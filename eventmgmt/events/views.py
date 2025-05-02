# events/views.py

from django.views.generic import TemplateView, ListView
from .models import Event

class MonthListView(TemplateView):
    template_name = 'events/months.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months'] = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return context

class EventListView(ListView):
    template_name = 'events/events.html'
    context_object_name = 'events'
    model = Event

    def get_queryset(self):
        return Event.objects.filter(month=self.kwargs['month'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = self.kwargs['month']
        return context

from django.views.generic import TemplateView
from .models import Ticket


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["tickets"] = Ticket.objects.all()
        return context

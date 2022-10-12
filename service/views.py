from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["message"] = "Hey"
        return context

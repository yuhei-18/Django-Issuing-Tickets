from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = self.get_context_data(**kwargs)
        context["message"] = "HeyHey"
        context["price"] = 100
        return self.render_to_response(context)

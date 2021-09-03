from django.views.generic import TemplateView


class HomePage(TemplateView):
    """Pagina Principal"""
    template_name = "home/principal.html"

    def get_context_data(self, **kwargs):
        args = dict()
        return args
from django.views.generic import TemplateView


class ExamplePageView(TemplateView):
    template_name = 'core/pages/example_page.html'

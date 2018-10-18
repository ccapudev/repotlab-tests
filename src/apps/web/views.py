from django.shortcuts import render
from django.views.generic import TemplateView
from apps.core.pdf.tabla import create_pdf

class HomeView(TemplateView):
    template_name = "web/home.html"

    def get(self, request):
        if request.GET.get('pdf'):
            return create_pdf()
        return super().get(request)

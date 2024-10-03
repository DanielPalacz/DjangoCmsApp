from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render

# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = "core/index.html"
    # variable 'object_list' is pushed with context to template rendering
    # can be changed by:
    context_object_name = "index"


class SingleViw(DetailView):
    model = Core
    template_name = "core/single.html"
    context_object_name = "post"
    # here variable

from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = "core/index.html"
    # variable 'object_list' is pushed with context to template rendering
    # can be changed by:
    context_object_name = "index"


class SingleView(DetailView):
    model = Core
    template_name = "core/single.html"
    context_object_name = "post"
    # here variable 'context_object_name' is pushed with context to template rendering

class PostsView(ListView):
    model = Core
    template_name = "core/posts.html"
    context_object_name = "post_list"

class AddView(CreateView):
    model = Core
    # fields = ["name"]
    template_name = "core/add.html"
    fields = "__all__"
    success_url = reverse_lazy("core:posts")

class EditView(UpdateView):
    model = Core
    # fields = ["name"]
    template_name = "core/edit.html"
    fields = "__all__"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("core:posts")

class Delete(DeleteView):
    model = Core
    template_name = "core/confirm-delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("core:posts")

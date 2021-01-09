from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid


# Create your views here.


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    # queryset = Blog.objects.order_by('-publish_date')


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self, form):
        blog_object = form.save(commit=False)
        blog_object.author = self.request.user
        title = blog_object.blog_title
        blog_object.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_object.save()

        return HttpResponseRedirect(reverse('index'))

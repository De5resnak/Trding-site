from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post, Response, MemberUser
from .forms import ResponseForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-post_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

class CreateResponse(LoginRequiredMixin, CreateView):
    model = Response
    template_name = 'createresponse.html'
    form_class = ResponseForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)
        form.instance.post = post
        form.instance.sender = self.request.user
        return super().form_valid(form)

class DeleteResponse(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('post_list')

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        any_user = get_object_or_404(User, username=self.request.user)
        form.instance.member = get_object_or_404(MemberUser, anyUser=any_user)
        return super().form_valid(form)

def confirm_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    response.confirm()
    return redirect('post_list')

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
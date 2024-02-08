from django.shortcuts import render
from trade.models import Response, MemberUser, Post
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.
class profile(ListView):
    model = Response
    ordering = '-response_date'
    template_name = 'profile.html'

    def get_queryset(self):
        current_user = self.request.user
        user_posts = Post.objects.filter(member=current_user.memberuser)
        queryset = Response.objects.filter(post__in=user_posts)
        queryset = queryset.filter(confirmation=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

    paginate_by = 10

    paginate_by = 10
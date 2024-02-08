from django.contrib import admin
from .models import Post, MemberUser, Response

admin.site.register(Post)
admin.site.register(MemberUser)
admin.site.register(Response)
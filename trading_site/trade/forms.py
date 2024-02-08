from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Response
from ckeditor.widgets import CKEditorWidget

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']

        def __init__(self, *args, **kwargs):
            post_id = kwargs.pop('post', None)
            super(ResponseForm, self).__init__(*args, **kwargs)

            if post_id:
                self.fields['post'].queryset = Post.objects.filter(pk=post_id)
            else:
                self.fields['post'].queryset = Post.objects.all()

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['content','category','title']

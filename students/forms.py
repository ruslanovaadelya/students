from django import forms
from .models import Comment


class CommentsFormat(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text_comment')
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(label_suffix=":",
                              widget=forms.Textarea(
                                  attrs={'required': False,
                                         'cols': 20, 'rows': 10,
                                         'placeholder': "Enter your content here."}))

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
                  'categories', 'featured', 'previous_post', 'next_post')
        widgets = {
            'overview': forms.Textarea(attrs={'placeholder': 'Blog overview here.....'})
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ('content', )

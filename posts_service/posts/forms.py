from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['userId', 'title', 'body']


class GetPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['userId']


class UpdatePostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if not title:
            cleaned_data['title'] = self.instance.title
        body = cleaned_data.get('body')
        if not body:
            cleaned_data['body'] = self.instance.body
        user_id = self.instance.userId
        if 'userId' in self.data and self.data['userId'] != user_id:
            raise forms.ValidationError("Changing the user id is not permitted.")
        post_id = self.instance.id
        if 'id' in self.data and self.data['id'] != post_id:
            raise forms.ValidationError("Changing the post id is not permitted.")
        return cleaned_data

import json
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from rest_framework import serializers
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import Post
from .forms import UpdatePostForm, CreatePostForm
from .serializers import PostSerializer


class CreatePostSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()


class UpdatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()


class RetrievePostByPostIdView(APIView):
    def get(self, request, post_id=None):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            # Post not found in the system, fetch from external API
            external_api_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            response = requests.get(external_api_url)
            if response.status_code == 200:
                post_data = response.json()
                # Create a new post using the fetched data
                post = Post.objects.create(id=post_data['id'], userId=post_data['userId'], title=post_data['title'],
                                           body=post_data['body'])
            else:
                # Post not found in the external API as well
                return HttpResponseNotFound(f"No posts found for the given post ID: {post_id}")

        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)


class RetrievePostByUserIdView(APIView):
    def get(self, request, user_id=None):
            posts = Post.objects.filter(userId=user_id)
            if not posts:
                return HttpResponseNotFound(f"No posts found for the given user ID: {user_id}")
            data = [{'id': post.id, 'userId': post.userId, 'title': post.title, 'body': post.body} for post in posts]
            return JsonResponse(data, safe=False)


class UpdatePostView(APIView):
    @swagger_auto_schema(request_body=UpdatePostSerializer)
    def patch(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        form = UpdatePostForm(data=data, instance=post)
        if form.is_valid():
            if 'title' in form.cleaned_data:
                post.title = form.cleaned_data['title']
            if 'body' in form.cleaned_data:
                post.body = form.cleaned_data['body']
            post.save()
            serializer = PostSerializer(post)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'errors': form.errors}, status=400)


class CreatePostView(APIView):

    @swagger_auto_schema(request_body=CreatePostSerializer)
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        form = CreatePostForm(data=data)#, instance=post)
        if not form.is_valid():
            return JsonResponse({'errors': form.errors}, status=400)
        user_id = form.cleaned_data['userId']
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']

        # Validate the userId using the external API
        if self.validate_user_id(user_id):
            # Create a new post in the database
            post = Post(userId=user_id, title=title, body=body)
            post.save()
            return JsonResponse({'message': 'Post created successfully.'})
        else:
            return JsonResponse({'message': 'Invalid userId.'}, status=400)

    # Helper functions for external API interactions
    def validate_user_id(self, user_id):
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        if response.status_code == 200:
            return True
        return False


class DeletePostView(APIView):
    def delete(self, request, post_id):
        # Retrieve the post to be deleted
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return JsonResponse({'message': 'Post deleted successfully.'})


def retrieve_posts_by_user_id(user_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={user_id}')
    if response.status_code == 200:
        posts_data = response.json()
        posts = []
        for post_data in posts_data:
            post = Post(userId=user_id, id=post_data['id'], title=post_data['title'], body=post_data['body'])
            post.save()
            posts.append(post)
        return posts
    return []
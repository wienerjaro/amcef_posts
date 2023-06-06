from django.urls import path
from .views import CreatePostView, RetrievePostByPostIdView, RetrievePostByUserIdView, UpdatePostView, DeletePostView

app_name = 'posts'

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='post_create'),
    path('<int:post_id>/', RetrievePostByPostIdView.as_view(), name='retrieve_post_by_id'),
    path('user/<int:user_id>/', RetrievePostByUserIdView.as_view(), name='retrieve_post_by_user_id'),
    path('<int:post_id>/update/', UpdatePostView.as_view(), name='update_post'),
    path('<int:post_id>/delete/', DeletePostView.as_view(), name='delete_post'),
]
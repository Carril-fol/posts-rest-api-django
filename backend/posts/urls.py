from django.urls import path
from .views import *

urlpatterns = [
    # Posts URLS
    path('api/get-post/<int:post_id>/', get_post, name='get-post'),
    path('api/builder-post/', create_post, name='builder-posts'),
    path('api/update-post/<int:post_id>/', update_post, name='updater-posts'),
    path('api/delete-post/<int:post_id>/', delete_post, name='deleter-posts'),
    path('api/detail-post/<int:post_id>/', detail_post, name='detail-posts'),
    path('api/all-posts/', get_all_posts, name='get-all-posts'),
    # Comment URLS
    path('api/builder-comment/<int:post_id>/', create_comment, name='builder-comment'),
    path('api/update-comment/<int:comment_id>/', update_comment, name='updater-comment'),
    path('api/delete-comment/<int:comment_id>/', delete_comment, name='deleter-comment'),
    # Like URLS
    path('api/like-posts/<int:post_id>/<int:user_id>/', like_posts, name='like-posts'),
    path('api/like-comments/<int:comment_id>/<int:user_id>/', like_comment, name='like-comments'),
    
]
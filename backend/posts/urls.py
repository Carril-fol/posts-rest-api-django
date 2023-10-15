from django.urls import path
from . import views

urlpatterns = [
    # Posts URLS
    path('api/get-post/<int:post_id>/', views.get_post, name='get-post'),
    path('api/builder-post/', views.create_post, name='builder-posts'),
    path('api/update-post/<int:post_id>/', views.update_post, name='updater-posts'),
    path('api/delete-post/<int:post_id>/', views.delete_post, name='deleter-posts'),
    path('api/detail-post/<int:post_id>/', views.detail_post, name='detail-posts'),

    # Comment URLS
    path('api/builder-comment/<int:post_id>/', views.create_comment, name='builder-comment'),
    path('api/update-comment/<int:comment_id>/', views.update_comment, name='updater-comment'),
    path('api/delete-comment/<int:comment_id>/', views.delete_comment, name='deleter-comment'),
    
    # Like URLS
    path('api/like-posts/<int:post_id>/<int:user_id>/', views.like_posts, name='like-posts'),
    path('api/like-comments/<int:comment_id>/<int:user_id>/', views.like_comment, name='like-comments'),

]
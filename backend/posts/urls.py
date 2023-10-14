from django.urls import path
from . import views

urlpatterns = [
    path('api/get-post/<int:post_id>/', views.get_post, name='get-post'),
    path('api/builder-post/', views.create_post, name='builder-posts'),
    path('api/update-post/<int:post_id>/', views.update_post, name='updater-posts'),
    path('api/delete-post/<int:post_id>/', views.delete_post, name='deleter-posts')
]
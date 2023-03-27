from django.urls import path
from comment.views import comment_home_view, comment_detail_view, comment_update_view, comment_delete_view

urlpatterns = [
    path('', comment_home_view, name='home'),
    path('/<int:pk>/detail', comment_detail_view, name='detail'),
    path('/<int:pk>/update', comment_update_view, name='update'),
    path('/<int:pk>/delete', comment_delete_view, name='delete'),
]


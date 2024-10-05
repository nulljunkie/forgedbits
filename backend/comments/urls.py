from django.urls import path

from .views import CommentView, CreateCommentView

urlpatterns = [
    path("post/<slug:post_id>", CommentView.as_view(), name="api_all_comments"),
    path('add/', CreateCommentView.as_view(), name="api_create_comment")
]


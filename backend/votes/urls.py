from django.urls import path

from .views import VoteView

urlpatterns = [
    path("vote/", VoteView.as_view(), name="api_post_vote"),
    path("vote/delete/<int:pk>", VoteView.as_view(), name="api_vote_delete"),
    path("vote/update/<int:pk>", VoteView.as_view(), name="api_vote_update"),
]

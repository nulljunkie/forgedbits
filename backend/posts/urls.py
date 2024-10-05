from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CreatePostView, MyPostsListView, PostDetailView,
                    PostListByTagView, PostListView, SavedPosts, SearchView,
                    TagsView)

router = DefaultRouter()
router.register(r'create', CreatePostView)

urlpatterns = [
    path("", PostListView.as_view(), name="api_post_list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="api_post_get_by_id"),
    path("tags/", TagsView.as_view(), name="api_get_all_tags"),
    path("tag/<slug:tag>", PostListByTagView.as_view(), name="api_get_post_list_by_tag"),
    path("search", SearchView.as_view(), name="search_view"),
    path("saved/", SavedPosts.as_view(), name="api_saved_posts"),
    path("me/", MyPostsListView.as_view(), name="api_my_posts"),
    path('', include(router.urls)),
]




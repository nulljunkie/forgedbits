from rest_framework.generics import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Post


#WARN: database query inside the permission class can cause performace issues
class ReadOnlyWriteOnlyByAuthor(BasePermission):

    def has_permission(self, request, view):

        pk = view.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)

        is_authenticated = bool(request.user and request.user.is_authenticated)
        is_author = bool(request.user == post.author)

        return bool(
            request.method in ('GET', 'HEAD', 'OPTIONS') or is_authenticated and is_author
        )


class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user

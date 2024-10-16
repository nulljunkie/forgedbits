from rest_framework import permissions


class IsChatParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.alice == request.user or obj.bob == request.user


class IsUserInvolvedInChatCreation(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return True

    def has_create_permission(self, request, view):
        data = request.data
        print('permissions: ', data)
        alice = data.get('alice')
        bob = data.get('bob')
        
        return str(request.user.username) in [str(alice), str(bob)]

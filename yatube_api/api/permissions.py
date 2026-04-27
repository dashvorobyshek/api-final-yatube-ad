from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        if hasattr(obj, 'author'):
            return obj.author == request.user
        return obj.author == request.user

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        return True

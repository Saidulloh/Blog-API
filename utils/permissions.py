from rest_framework.permissions import BasePermission


class UserIsOwner(BasePermission):
    """
    For model User
    """
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsOwner(BasePermission):
    """
    For other model
    """
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.owner.id

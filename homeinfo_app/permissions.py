from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff
    



class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_staff or obj.owner == request.user:
            return True

        return False
    
    


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow administrators to have full access
    and provide read-only access to other users.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to administrators
        return request.user and request.user.is_staff


class Is_client(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and not request.user.is_staff

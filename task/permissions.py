from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user == obj.user


class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

from rest_framework import permissions
from rest_framework.permissions import BasePermission


class VehiculoPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

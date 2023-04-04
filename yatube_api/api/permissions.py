from rest_framework.permissions import (
    SAFE_METHODS, BasePermission
)


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

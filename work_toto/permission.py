
from rest_framework.permissions import BasePermission


class Permission(BasePermission):

    def has_permission(self, request, view):
        if request.session.get('userinfo') is not None:
            res = True
        else:
            res = False
        return res
        
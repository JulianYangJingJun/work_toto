from rest_framework.permissions import BasePermission
from config.settings import base as BASE


class Permission(BasePermission):
    def has_permission(self, request, view):
        ips = BASE.PERMISSION_HOSTS
        remote_ip = request.META['REMOTE_ADDR']
        if remote_ip in ips:
            return True
        else:
            if bool(request.user):
                return True
            return False
        # return bool(request.user)
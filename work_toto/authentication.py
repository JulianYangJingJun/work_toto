
from django.conf import settings
from rest_framework.authentication import BaseAuthentication

EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)


class Authentication(BaseAuthentication):

    def authenticate(self, request):

        user = getattr(request._request, 'user', None)

        if not user:
            return None
        '''TODO:进一步确认user'''

        return (user, None)
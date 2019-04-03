
from django.conf import settings
from rest_framework.authentication import BaseAuthentication


EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        return request.session.get('userinfo'), None
        # user = getattr(request._request, 'userinfo', None)

        # if not user:
        #     return None
        # '''TODO:进一步确认user'''

        # return (user, None)

'''
JulianYangjingjun
yjj12345
'''
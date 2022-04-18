from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=user)
            # message = 'Su Token ha expirado'
        return is_expired,token



    def authenticate_credentials(self, key):
        message,token,user = None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Invalido'
            self.expired = True

        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado'
            is_expired = self.token_expire_handler(token)
            if is_expired:
                message = 'Su token ha expirado'
        return user, token, message, self.expired



# model = self.get_model()
# try:
#     token = model.objects.select_related('user').get(key=key)
# except model.DoesNotExist:
#     raise exceptions.AuthenticationFailed(_('Invalid token.'))
#
# if not token.user.is_active:
#     raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
#
# return (token.user, token)

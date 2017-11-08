"""Configure and hold relevant security information for the app."""
import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Authenticated
from pyramid.security import Allow
from passlib.apps import custom_app_context as pwd_context


class MyRoot(object):

    def __init__(self, request):
        """."""
        self.request = request

    __acl__ = [
        (Allow, Authenticated, 'secret'),
    ]


def is_authenticated(username, password):
    """Verify the username and password entered by user."""
    stored_username = os.environ.get('AUTH_USERNAME', '')
    stored_password = os.environ.get('AUTH_PASSWORD', '')
    authenticated = False
    if stored_username and stored_password:
        try:
            authenticated = pwd_context.verify(password, stored_password)
        except ValueError:
            pass
    return authenticated


def includeme(config):
    """Tell pyramid to include this function with the view config."""
    # authentication
    auth_secret = os.environ.get('AUTH_SECRET', '')
    auth_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )
    config.set_authentication_policy(auth_policy)

    # authorization
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(MyRoot)
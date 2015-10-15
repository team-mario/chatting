__author__ = 'judelee'

from authomatic.providers import oauth2

CONFIG = {
    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '915525561856065',
        'consumer_secret': '428aaf2ee45ccb6a9221e5eb4d760842',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['email', 'public_profile'],
    }
}
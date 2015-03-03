import uuid
import re
import python_oauth2.oauth2 as oauth
import time
from lti_constants import *


def sign_request(params, url, method, key, secret):
    # Create our request. Change method, etc. accordingly.
    req = oauth.Request(method=method, url=url, parameters=params, is_form_encoded=True)

    _consumer = oauth.Consumer(key=key, secret=secret)

    # Sign the request.
    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, _consumer, token=None)
    return req


def prepare_oauth_params(params, key):
    params[OAUTH_PREFIX + 'version'] = '1.0'
    params[OAUTH_PREFIX + 'nonce'] = oauth.generate_nonce()
    params[OAUTH_PREFIX + 'timestamp'] = int(time.time())
    params[OAUTH_PREFIX + 'consumer_key'] = key
    params[OAUTH_PREFIX + 'signature_method'] = 'HMAC-SHA1'


def prepare_lti_params(params):
    if LTI_VERSION not in params:
        params[LTI_VERSION] = LTI_VERSION_1

    if LTI_MESSAGE_TYPE not in params:
        params[LTI_MESSAGE_TYPE] = LTI_MESSAGE_TYPE_BASICLTILAUNCHREQUEST

    if RESOURCE_LINK_ID not in params:
        params[RESOURCE_LINK_ID] = uuid.uuid1().__str__()

#   any non-standard param should be converted to custom_param
#   also any key character matching [^A-Za-z0-9] will be replaced by _
    for key in params:
        if key not in valid_property_names and \
                not str(key).startswith(CUSTOM_PREFIX) and \
                not str(key).startswith(EXTENSION_PREFIX):
            temp = params[key]
            del params[key]
            params[CUSTOM_PREFIX + re.sub(r"[^A-Za-z0-9]", r"_", key)] = temp


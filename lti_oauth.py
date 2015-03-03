from lti_constants import *
import uuid


def sign_request(params, url, method, consumer, secret):
    pass


def lti_params(params):
    if LTI_VERSION not in params:
        params[LTI_VERSION] = LTI_VERSION_1

    if LTI_MESSAGE_TYPE not in params:
        params[LTI_MESSAGE_TYPE] = LTI_MESSAGE_TYPE_BASICLTILAUNCHREQUEST

    if RESOURCE_LINK_ID not in params:
        params[RESOURCE_LINK_ID] = uuid.uuid1().__str__()

#   any non-standard param should be converted to custom_param
    for key in params:
        if key not in valid_property_names and \
                not str(key).startswith(CUSTOM_PREFIX) and \
                not str(key).startswith(EXTENSION_PREFIX):
            temp = params[key]
            del params[key]
            params[CUSTOM_PREFIX + key] = temp
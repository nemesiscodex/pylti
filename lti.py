import uuid
import re
import python_oauth2.oauth2 as oauth
import time
from lti_constants import *


def get_lti_form(params, url, key, secret):
    """
    Get basic lti launch auto-submit form
    :param params: mutable map of raw parameters
    :param url: non-mutable lti endpoint
    :param key: non-mutable consumer key
    :param secret: non-mutable consumer secret
    :return: html string of the form + auto-submit script
    """
    prepare_lti_params(params)
    prepare_oauth_params(params, key)
    request = sign_request(params, url, 'POST', key, secret)
    html = "<form action='%s' name=\"ltiLaunchForm\" method=\"POST\" encType=\"application/x-www-form-urlencoded\">\n" % url
    for key in request.keys():
        html += "<input type=\"hidden\" name=\"%s\" value=\"%s\">\n" % (html_special_chars(key),
                                                                        html_special_chars(request.get_parameter(key)))
    html += "</form>\n"
    html += "<script language=\"javascript\">\n"
    html += "document.ltiLaunchForm.submit();\n"
    html += "</script>"
    return html


def html_special_chars(value):
    """
    Scape html special characters
    :param value: value
    :return: scaped value
    """
    ret_val = re.sub(r"&", r"&amp;", str(value))
    ret_val = re.sub(r"\"", r"&quot;", ret_val)
    ret_val = re.sub(r"<", r"&lt;", ret_val)
    ret_val = re.sub(r">", r"&gt;", ret_val)
    ret_val = re.sub(r">", r"&gt;", ret_val)
    ret_val = re.sub(r"=", r"&#61;", ret_val)
    return ret_val


def sign_request(params, url, method, key, secret):
    """
    Obtain a signed request using HMAC-SHA1
    :param params: mutable request parameter map
    :param url: non-mutable destination url
    :param method: non-mutable method used (e.g. POST, GET, etc)
    :param key: non-mutable consumer key
    :param secret: non-mutable consumer secret
    :return: signed http request
    """
    # Create our request. Change method, etc. accordingly.
    req = oauth.Request(method=method, url=url, parameters=params, is_form_encoded=True)

    _consumer = oauth.Consumer(key=key, secret=secret)

    # Sign the request.
    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, _consumer, token=None)
    return req


def prepare_oauth_params(params, key):
    """
    Prepare Oauth parameters
    :param params: mutable initial request parameter map
    :param key: non-mutable consumer key
    """
    params[OAUTH_PREFIX + 'version'] = '1.0'
    params[OAUTH_PREFIX + 'nonce'] = oauth.generate_nonce()
    params[OAUTH_PREFIX + 'timestamp'] = int(time.time())
    params[OAUTH_PREFIX + 'consumer_key'] = key
    params[OAUTH_PREFIX + 'signature_method'] = 'HMAC-SHA1'


def prepare_lti_params(params):
    """
    Prepare basic lti launch parameters
    Adds LTI_VERSION, LTI_MESSAGE_TYPE, RESOURCE_LINK_ID (a random value)
    Replaces custom parameter names, replacing special characters with _, and adding a CUSTOM_PREFIX
    :param params: mutable initial parameter map
    :return:
    """
    if LTI_VERSION not in params:
        params[LTI_VERSION] = LTI_VERSION_1

    if LTI_MESSAGE_TYPE not in params:
        params[LTI_MESSAGE_TYPE] = LTI_MESSAGE_TYPE_BASICLTILAUNCHREQUEST

    if RESOURCE_LINK_ID not in params:
        params[RESOURCE_LINK_ID] = uuid.uuid1().__str__()

    # any non-standard param should be converted to custom_param
    # also any key character matching [^A-Za-z0-9] will be replaced by _
    for key in params:
        if key not in valid_property_names and \
                not str(key).startswith(CUSTOM_PREFIX) and \
                not str(key).startswith(EXTENSION_PREFIX):
            temp = params[key]
            del params[key]
            params[CUSTOM_PREFIX + re.sub(r"[^A-Za-z0-9]", r"_", key)] = temp


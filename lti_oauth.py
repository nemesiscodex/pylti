def sign_request(params, url, method, consumer, secret):
    pass

def check_params(params):
    if LTI_VERSION not in params:
        params[LTI_VERSION] = LTI_VERSION_1

    if LTI_MESSAGE_TYPE not in params:
        params[LTI_MESSAGE_TYPE] = LTI_MESSAGE_TYPE_BASICLTILAUNCHREQUEST

    if BASICLTI_SUBMIT not in params:
        params[BASICLTI_SUBMIT] = ""

    #any non-standard param should be converted to ext_param or custom_param

    

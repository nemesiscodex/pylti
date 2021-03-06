"""
LTI constants (LTI v1.0, LTI v2.0)
"""

CONTEXT_ID = "context_id"

CONTEXT_LABEL = "context_label"

CONTEXT_TITLE = "context_title"

CONTEXT_TYPE = "context_type"

CONTEXT_TYPE_COURSE_OFFERING = "CourseOffering"

CONTEXT_TYPE_COURSE_SECTION = "CourseSection"

CONTEXT_TYPE_COURSE_TEMPLATE = "CourseTemplate"

CONTEXT_TYPE_GROUP = "GROUP"

EXTENSION_PREFIX = "ext_"

CUSTOM_PREFIX = "custom_"

OAUTH_PREFIX = "oauth_"

LAUNCH_PRESENTATION_DOCUMENT_TARGET = "launch_presentation_document_target"

LAUNCH_PRESENTATION_HEIGHT = "launch_presentation_height"

LAUNCH_PRESENTATION_LOCALE = "launch_presentation_locale"

LAUNCH_PRESENTATION_RETURN_URL = "launch_presentation_return_url"

LAUNCH_PRESENTATION_WIDTH = "launch_presentation_width"

LAUNCH_PRESENTATION_CSS_URL = "launch_presentation_css_url"

LIS_PERSON_CONTACT_EMAIL_PRIMARY = "lis_person_contact_email_primary"

LIS_PERSON_NAME_FAMILY = "lis_person_name_family"

LIS_PERSON_NAME_FULL = "lis_person_name_full"

LIS_PERSON_NAME_GIVEN = "lis_person_name_given"

LIS_PERSON_SOURCEDID = "lis_person_sourcedid"

LIS_COURSE_OFFERING_SOURCEDID = "lis_course_offering_sourcedid"

LIS_COURSE_SECTION_SOURCEDID = "lis_course_section_sourcedid"

LIS_OUTCOME_SERVICE_URL = "lis_outcome_service_url"

LIS_RESULT_SOURCEDID = "lis_result_sourcedid"

IS_RESULT_SOURCEDID = "lis_result_sourcedid"

LTI_MESSAGE_TYPE = "lti_message_type"

LTI_MESSAGE_TYPE_TOOLPROXYREGISTRATIONREQUEST = "ToolProxyRegistrationRequest"

LTI_MESSAGE_TYPE_TOOLPROXY_RE_REGISTRATIONREQUEST = "ToolProxyReregistrationRequest"

LTI_MESSAGE_TYPE_BASICLTILAUNCHREQUEST = "basic-lti-launch-request"

LTI_VERSION = "lti_version"

LTI_VERSION_1 = "LTI-1p0"

LTI_VERSION_2 = "LTI-2p0"

TOOL_CONSUMER_INFO_PRODUCT_FAMILY_CODE = "tool_consumer_info_product_family_code"

TOOL_CONSUMER_INFO_VERSION = "tool_consumer_info_version"

RESOURCE_LINK_ID = "resource_link_id"

RESOURCE_LINK_TITLE = "resource_link_title"

RESOURCE_LINK_DESCRIPTION = "resource_link_description"

ROLES = "roles"

TC_PROFILE_URL = "tc_profile_url"

TOOL_CONSUMER_INSTANCE_CONTACT_EMAIL = "tool_consumer_instance_contact_email"

TOOL_CONSUMER_INSTANCE_DESCRIPTION = "tool_consumer_instance_description"

TOOL_CONSUMER_INSTANCE_GUID = "tool_consumer_instance_guid"

TOOL_CONSUMER_INSTANCE_NAME = "tool_consumer_instance_name"

TOOL_CONSUMER_INSTANCE_URL = "tool_consumer_instance_url"

USER_ID = "user_id"

USER_IMAGE = "user_image"

valid_property_names = [CONTEXT_ID,
                        CONTEXT_LABEL, CONTEXT_TITLE, CONTEXT_TYPE,
                        LAUNCH_PRESENTATION_DOCUMENT_TARGET, LAUNCH_PRESENTATION_HEIGHT,
                        LAUNCH_PRESENTATION_LOCALE, LAUNCH_PRESENTATION_RETURN_URL,
                        LAUNCH_PRESENTATION_WIDTH, LIS_PERSON_CONTACT_EMAIL_PRIMARY,
                        LAUNCH_PRESENTATION_CSS_URL,
                        TOOL_CONSUMER_INFO_PRODUCT_FAMILY_CODE,
                        TOOL_CONSUMER_INFO_VERSION,
                        LIS_PERSON_NAME_FAMILY, LIS_PERSON_NAME_FULL, LIS_PERSON_NAME_GIVEN,
                        LIS_PERSON_SOURCEDID, LIS_COURSE_OFFERING_SOURCEDID,
                        LIS_COURSE_SECTION_SOURCEDID,
                        LIS_OUTCOME_SERVICE_URL, LIS_RESULT_SOURCEDID,
                        LTI_MESSAGE_TYPE, LTI_VERSION, RESOURCE_LINK_ID,
                        RESOURCE_LINK_TITLE, RESOURCE_LINK_DESCRIPTION, ROLES,
                        TC_PROFILE_URL,
                        TOOL_CONSUMER_INSTANCE_CONTACT_EMAIL, TOOL_CONSUMER_INSTANCE_DESCRIPTION,
                        TOOL_CONSUMER_INSTANCE_GUID, TOOL_CONSUMER_INSTANCE_NAME,
                        TOOL_CONSUMER_INSTANCE_URL, USER_ID, USER_IMAGE]



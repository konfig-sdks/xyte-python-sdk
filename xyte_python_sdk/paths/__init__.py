# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from xyte_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_DEVICES = "/v1/devices"
    V1_DEVICES_PARENT_ID_CHILDREN = "/v1/devices/{parent_id}/children"
    V1_DEVICES_DEVICE_ID = "/v1/devices/{deviceId}"
    V1_DEVICES_DEVICE_ID_CLOUD_SETTINGS = "/v1/devices/{deviceId}/cloud_settings"
    V1_DEVICES_DEVICE_ID_TELEMETRY = "/v1/devices/{deviceId}/telemetry"
    V1_DEVICES_DEVICE_ID_CHILDREN_TELEMETRIES = "/v1/devices/{deviceId}/children/telemetries"
    V1_DEVICES_DEVICE_ID_CONFIG = "/v1/devices/{deviceId}/config"
    V1_DEVICES_DEVICE_ID_COMMAND = "/v1/devices/{deviceId}/command"
    V1_DEVICES_DEVICE_ID_DUMPS_MIMETYPE_FILENAME = "/v1/devices/{deviceId}/dumps/{mime-type}/{filename}"
    V1_DEVICES_DEVICE_ID_DUMPS_DUMP_ID = "/v1/devices/{deviceId}/dumps/{dumpId}"
    V1_DEVICES_DEVICE_ID_LICENSES = "/v1/devices/{deviceId}/licenses"
    V1_DEVICES_DEVICE_ID_LICENSE = "/v1/devices/{deviceId}/license"
    V1_DEVICES_DEVICE_ID_SPACE = "/v1/devices/{deviceId}/space"
    V1_DEVICES_DEVICE_ID_FILES_FILE_UUID = "/v1/devices/{deviceId}/files/{fileUuid}"
    V1_DEVICES_DEVICE_ID_FILES = "/v1/devices/{deviceId}/files"
    V1_DEVICES_DEVICE_ID_INCIDENTS = "/v1/devices/{deviceId}/incidents"
    V1_DEVICES_DEVICE_ID_INCIDENTS_INCIDENT_ID = "/v1/devices/{deviceId}/incidents/{incidentId}"
    CORE_V1_PARTNER_DEVICES = "/core/v1/partner/devices"
    CORE_V1_PARTNER_DEVICES_DEVICE_ID = "/core/v1/partner/devices/{device_id}"
    CORE_V1_PARTNER_DEVICES_DEVICE_ID_TELEMETRIES = "/core/v1/partner/devices/{device_id}/telemetries"
    CORE_V1_PARTNER_DEVICES_DEVICE_ID_CONFIG = "/core/v1/partner/devices/{device_id}/config"
    CORE_V1_PARTNER_DEVICES_DEVICE_ID_COMMANDS = "/core/v1/partner/devices/{device_id}/commands"
    CORE_V1_PARTNER_DEVICES_DEVICE_ID_HISTORY = "/core/v1/partner/devices/{device_id}/history"
    CORE_V1_PARTNER_DEVICES_HISTORIES = "/core/v1/partner/devices/histories"
    CORE_V1_PARTNER_TICKETS = "/core/v1/partner/tickets"
    CORE_V1_PARTNER_TICKETS_TICKET_ID_COPY = "/core/v1/partner/tickets/{ticket_id} (COPY)"
    CORE_V1_PARTNER_TICKETS_TICKET_ID = "/core/v1/partner/tickets/{ticket_id}"
    CORE_V1_PARTNER_TICKETS_TICKET_ID_RESOLVED = "/core/v1/partner/tickets/{ticket_id}/resolved"
    CORE_V1_PARTNER_TICKETS_TICKET_ID_MESSAGE = "/core/v1/partner/tickets/{ticket_id}/message"

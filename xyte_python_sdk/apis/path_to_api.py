import typing_extensions

from xyte_python_sdk.paths import PathValues
from xyte_python_sdk.apis.paths.v1_devices import V1Devices
from xyte_python_sdk.apis.paths.v1_devices_parent_id_children import V1DevicesParentIdChildren
from xyte_python_sdk.apis.paths.v1_devices_device_id import V1DevicesDeviceId
from xyte_python_sdk.apis.paths.v1_devices_device_id_cloud_settings import V1DevicesDeviceIdCloudSettings
from xyte_python_sdk.apis.paths.v1_devices_device_id_telemetry import V1DevicesDeviceIdTelemetry
from xyte_python_sdk.apis.paths.v1_devices_device_id_children_telemetries import V1DevicesDeviceIdChildrenTelemetries
from xyte_python_sdk.apis.paths.v1_devices_device_id_config import V1DevicesDeviceIdConfig
from xyte_python_sdk.apis.paths.v1_devices_device_id_command import V1DevicesDeviceIdCommand
from xyte_python_sdk.apis.paths.v1_devices_device_id_dumps_mime_type_filename import V1DevicesDeviceIdDumpsMimeTypeFilename
from xyte_python_sdk.apis.paths.v1_devices_device_id_dumps_dump_id import V1DevicesDeviceIdDumpsDumpId
from xyte_python_sdk.apis.paths.v1_devices_device_id_licenses import V1DevicesDeviceIdLicenses
from xyte_python_sdk.apis.paths.v1_devices_device_id_license import V1DevicesDeviceIdLicense
from xyte_python_sdk.apis.paths.v1_devices_device_id_space import V1DevicesDeviceIdSpace
from xyte_python_sdk.apis.paths.v1_devices_device_id_files_file_uuid import V1DevicesDeviceIdFilesFileUuid
from xyte_python_sdk.apis.paths.v1_devices_device_id_files import V1DevicesDeviceIdFiles
from xyte_python_sdk.apis.paths.v1_devices_device_id_incidents import V1DevicesDeviceIdIncidents
from xyte_python_sdk.apis.paths.v1_devices_device_id_incidents_incident_id import V1DevicesDeviceIdIncidentsIncidentId
from xyte_python_sdk.apis.paths.core_v1_partner_devices import CoreV1PartnerDevices
from xyte_python_sdk.apis.paths.core_v1_partner_devices_device_id import CoreV1PartnerDevicesDeviceId
from xyte_python_sdk.apis.paths.core_v1_partner_devices_device_id_telemetries import CoreV1PartnerDevicesDeviceIdTelemetries
from xyte_python_sdk.apis.paths.core_v1_partner_devices_device_id_config import CoreV1PartnerDevicesDeviceIdConfig
from xyte_python_sdk.apis.paths.core_v1_partner_devices_device_id_commands import CoreV1PartnerDevicesDeviceIdCommands
from xyte_python_sdk.apis.paths.core_v1_partner_devices_device_id_history import CoreV1PartnerDevicesDeviceIdHistory
from xyte_python_sdk.apis.paths.core_v1_partner_devices_histories import CoreV1PartnerDevicesHistories
from xyte_python_sdk.apis.paths.core_v1_partner_tickets import CoreV1PartnerTickets
from xyte_python_sdk.apis.paths.core_v1_partner_tickets_ticket_id__copy import CoreV1PartnerTicketsTicketIdCOPY
from xyte_python_sdk.apis.paths.core_v1_partner_tickets_ticket_id import CoreV1PartnerTicketsTicketId
from xyte_python_sdk.apis.paths.core_v1_partner_tickets_ticket_id_resolved import CoreV1PartnerTicketsTicketIdResolved
from xyte_python_sdk.apis.paths.core_v1_partner_tickets_ticket_id_message import CoreV1PartnerTicketsTicketIdMessage

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_DEVICES: V1Devices,
        PathValues.V1_DEVICES_PARENT_ID_CHILDREN: V1DevicesParentIdChildren,
        PathValues.V1_DEVICES_DEVICE_ID: V1DevicesDeviceId,
        PathValues.V1_DEVICES_DEVICE_ID_CLOUD_SETTINGS: V1DevicesDeviceIdCloudSettings,
        PathValues.V1_DEVICES_DEVICE_ID_TELEMETRY: V1DevicesDeviceIdTelemetry,
        PathValues.V1_DEVICES_DEVICE_ID_CHILDREN_TELEMETRIES: V1DevicesDeviceIdChildrenTelemetries,
        PathValues.V1_DEVICES_DEVICE_ID_CONFIG: V1DevicesDeviceIdConfig,
        PathValues.V1_DEVICES_DEVICE_ID_COMMAND: V1DevicesDeviceIdCommand,
        PathValues.V1_DEVICES_DEVICE_ID_DUMPS_MIMETYPE_FILENAME: V1DevicesDeviceIdDumpsMimeTypeFilename,
        PathValues.V1_DEVICES_DEVICE_ID_DUMPS_DUMP_ID: V1DevicesDeviceIdDumpsDumpId,
        PathValues.V1_DEVICES_DEVICE_ID_LICENSES: V1DevicesDeviceIdLicenses,
        PathValues.V1_DEVICES_DEVICE_ID_LICENSE: V1DevicesDeviceIdLicense,
        PathValues.V1_DEVICES_DEVICE_ID_SPACE: V1DevicesDeviceIdSpace,
        PathValues.V1_DEVICES_DEVICE_ID_FILES_FILE_UUID: V1DevicesDeviceIdFilesFileUuid,
        PathValues.V1_DEVICES_DEVICE_ID_FILES: V1DevicesDeviceIdFiles,
        PathValues.V1_DEVICES_DEVICE_ID_INCIDENTS: V1DevicesDeviceIdIncidents,
        PathValues.V1_DEVICES_DEVICE_ID_INCIDENTS_INCIDENT_ID: V1DevicesDeviceIdIncidentsIncidentId,
        PathValues.CORE_V1_PARTNER_DEVICES: CoreV1PartnerDevices,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID: CoreV1PartnerDevicesDeviceId,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_TELEMETRIES: CoreV1PartnerDevicesDeviceIdTelemetries,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_CONFIG: CoreV1PartnerDevicesDeviceIdConfig,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_COMMANDS: CoreV1PartnerDevicesDeviceIdCommands,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_HISTORY: CoreV1PartnerDevicesDeviceIdHistory,
        PathValues.CORE_V1_PARTNER_DEVICES_HISTORIES: CoreV1PartnerDevicesHistories,
        PathValues.CORE_V1_PARTNER_TICKETS: CoreV1PartnerTickets,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID_COPY: CoreV1PartnerTicketsTicketIdCOPY,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID: CoreV1PartnerTicketsTicketId,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID_RESOLVED: CoreV1PartnerTicketsTicketIdResolved,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID_MESSAGE: CoreV1PartnerTicketsTicketIdMessage,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_DEVICES: V1Devices,
        PathValues.V1_DEVICES_PARENT_ID_CHILDREN: V1DevicesParentIdChildren,
        PathValues.V1_DEVICES_DEVICE_ID: V1DevicesDeviceId,
        PathValues.V1_DEVICES_DEVICE_ID_CLOUD_SETTINGS: V1DevicesDeviceIdCloudSettings,
        PathValues.V1_DEVICES_DEVICE_ID_TELEMETRY: V1DevicesDeviceIdTelemetry,
        PathValues.V1_DEVICES_DEVICE_ID_CHILDREN_TELEMETRIES: V1DevicesDeviceIdChildrenTelemetries,
        PathValues.V1_DEVICES_DEVICE_ID_CONFIG: V1DevicesDeviceIdConfig,
        PathValues.V1_DEVICES_DEVICE_ID_COMMAND: V1DevicesDeviceIdCommand,
        PathValues.V1_DEVICES_DEVICE_ID_DUMPS_MIMETYPE_FILENAME: V1DevicesDeviceIdDumpsMimeTypeFilename,
        PathValues.V1_DEVICES_DEVICE_ID_DUMPS_DUMP_ID: V1DevicesDeviceIdDumpsDumpId,
        PathValues.V1_DEVICES_DEVICE_ID_LICENSES: V1DevicesDeviceIdLicenses,
        PathValues.V1_DEVICES_DEVICE_ID_LICENSE: V1DevicesDeviceIdLicense,
        PathValues.V1_DEVICES_DEVICE_ID_SPACE: V1DevicesDeviceIdSpace,
        PathValues.V1_DEVICES_DEVICE_ID_FILES_FILE_UUID: V1DevicesDeviceIdFilesFileUuid,
        PathValues.V1_DEVICES_DEVICE_ID_FILES: V1DevicesDeviceIdFiles,
        PathValues.V1_DEVICES_DEVICE_ID_INCIDENTS: V1DevicesDeviceIdIncidents,
        PathValues.V1_DEVICES_DEVICE_ID_INCIDENTS_INCIDENT_ID: V1DevicesDeviceIdIncidentsIncidentId,
        PathValues.CORE_V1_PARTNER_DEVICES: CoreV1PartnerDevices,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID: CoreV1PartnerDevicesDeviceId,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_TELEMETRIES: CoreV1PartnerDevicesDeviceIdTelemetries,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_CONFIG: CoreV1PartnerDevicesDeviceIdConfig,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_COMMANDS: CoreV1PartnerDevicesDeviceIdCommands,
        PathValues.CORE_V1_PARTNER_DEVICES_DEVICE_ID_HISTORY: CoreV1PartnerDevicesDeviceIdHistory,
        PathValues.CORE_V1_PARTNER_DEVICES_HISTORIES: CoreV1PartnerDevicesHistories,
        PathValues.CORE_V1_PARTNER_TICKETS: CoreV1PartnerTickets,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID_COPY: CoreV1PartnerTicketsTicketIdCOPY,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID: CoreV1PartnerTicketsTicketId,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID_RESOLVED: CoreV1PartnerTicketsTicketIdResolved,
        PathValues.CORE_V1_PARTNER_TICKETS_TICKET_ID_MESSAGE: CoreV1PartnerTicketsTicketIdMessage,
    }
)

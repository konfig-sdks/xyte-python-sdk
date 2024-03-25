operation_parameter_map = {
    '/v1/devices/{deviceId}/dumps/{dumpId}-PUT': {
        'parameters': [
            {
                'name': 'RAW_BODY'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'dumpId'
            },
        ]
    },
    '/v1/devices/{deviceId}/incidents/{incidentId}-DELETE': {
        'parameters': [
            {
                'name': 'deviceId'
            },
            {
                'name': 'incidentId'
            },
        ]
    },
    '/v1/devices-POST': {
        'parameters': [
            {
                'name': 'sn'
            },
            {
                'name': 'firmware_version'
            },
            {
                'name': 'hardware_key'
            },
            {
                'name': 'mac'
            },
            {
                'name': 'cloud_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'details'
            },
            {
                'name': 'sub_model'
            },
            {
                'name': 'parent_id'
            },
        ]
    },
    '/core/v1/partner/devices/{device_id}-DELETE': {
        'parameters': [
            {
                'name': 'device_id'
            },
        ]
    },
    '/core/v1/partner/devices/histories-GET': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/devices/{parent_id}/children-GET': {
        'parameters': [
            {
                'name': 'parent_id'
            },
        ]
    },
    '/v1/devices/{deviceId}/command-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/v1/devices/{deviceId}/config-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/core/v1/partner/devices/{device_id}/config-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
        ]
    },
    '/v1/devices/{deviceId}/files/{fileUuid}-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
            {
                'name': 'fileUuid'
            },
        ]
    },
    '/v1/devices/{deviceId}/files-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/v1/devices/{deviceId}/incidents-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/v1/devices/{deviceId}-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/core/v1/partner/devices/{device_id}-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
        ]
    },
    '/v1/devices/{deviceId}/license-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/v1/devices/{deviceId}/licenses-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/v1/devices/{deviceId}/space-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/core/v1/partner/devices/{device_id}/history-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v1/partner/devices/{device_id}/telemetries-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
        ]
    },
    '/core/v1/partner/devices/{device_id}/commands-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/core/v1/partner/devices-GET': {
        'parameters': [
            {
                'name': 'model_id'
            },
            {
                'name': 'sn'
            },
            {
                'name': 'mac'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/devices/{deviceId}/incidents-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'issue'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/v1/devices/{parent_id}/children-POST': {
        'parameters': [
            {
                'name': 'firmware_version'
            },
            {
                'name': 'model_id'
            },
            {
                'name': 'parent_id'
            },
            {
                'name': 'sub_model'
            },
            {
                'name': 'sn'
            },
            {
                'name': 'mac'
            },
            {
                'name': 'name'
            },
            {
                'name': 'details'
            },
        ]
    },
    '/v1/devices/{deviceId}/children/telemetries-POST': {
        'parameters': [
            {
                'name': 'RAW_BODY'
            },
            {
                'name': 'deviceId'
            },
        ]
    },
    '/v1/devices/{deviceId}/command-POST': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'id'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v1/devices/{deviceId}/dumps/{mime-type}/{filename}-POST': {
        'parameters': [
            {
                'name': 'RAW_BODY'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'mime-type'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/v1/devices/{deviceId}/telemetry-POST': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'timestamp'
            },
            {
                'name': 'telemetries'
            },
            {
                'name': 'override'
            },
        ]
    },
    '/v1/devices/{deviceId}/config-POST': {
        'parameters': [
            {
                'name': 'deviceId'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/v1/devices/{deviceId}/cloud_settings-PUT': {
        'parameters': [
            {
                'name': 'deviceId'
            },
            {
                'name': 'property'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/v1/devices/{deviceId}-PUT': {
        'parameters': [
            {
                'name': 'deviceId'
            },
            {
                'name': 'firmware_version'
            },
            {
                'name': 'name'
            },
            {
                'name': 'space_version'
            },
            {
                'name': 'config_version'
            },
            {
                'name': 'details'
            },
        ]
    },
    '/v1/devices/{deviceId}/licenses-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'state'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'error'
            },
        ]
    },
    '/core/v1/partner/tickets/{ticket_id}/message-POST': {
        'parameters': [
            {
                'name': 'ticket_id'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/core/v1/partner/tickets/{ticket_id}/resolved-POST': {
        'parameters': [
            {
                'name': 'ticket_id'
            },
        ]
    },
    '/core/v1/partner/tickets/{ticket_id} (COPY)-GET': {
        'parameters': [
            {
                'name': 'ticket_id'
            },
        ]
    },
    '/core/v1/partner/tickets-GET': {
        'parameters': [
        ]
    },
    '/core/v1/partner/tickets/{ticket_id}-PUT': {
        'parameters': [
            {
                'name': 'ticket_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
        ]
    },
};
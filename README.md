<div align="left">

[![Visit Xyte](./header.png)](https://xyte.io)

# Xyte<a id="xyte"></a>

Xyte's Device Cloud is the first all-in-one servitization platform designed for device and hardware manufacturers to cloudify, operate, support, and commercialize their connected devices in a unified platform. 

We enable OEMs across different industries to navigate their digital journey, transforming their devices into integrated business solutions that combine hardware, software and services. The only business and commerce platform designed specifically for IoT device manufacturers, our fully-federated Device Cloud empowers OEMs to manage the complete lifecycle of their devices, from the minute they leave the warehouse through aftermarket sales to end customers.

Our out-of-the-box applications for asset management, remote support, ecommerce and subscription management, financing, and a powerful and secure back office suite help OEMs boost revenue and market growth, optimize operational efficiencies, gain instant insights into equipment and device performance, and develop sustainable customer relationships.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`xyte.device.append_dump_file`](#xytedeviceappend_dump_file)
  * [`xyte.device.close_incident`](#xytedeviceclose_incident)
  * [`xyte.device.create_registration`](#xytedevicecreate_registration)
  * [`xyte.device.delete_device`](#xytedevicedelete_device)
  * [`xyte.device.get_all_device_state_histories`](#xytedeviceget_all_device_state_histories)
  * [`xyte.device.get_child_devices`](#xytedeviceget_child_devices)
  * [`xyte.device.get_command`](#xytedeviceget_command)
  * [`xyte.device.get_config`](#xytedeviceget_config)
  * [`xyte.device.get_config_0`](#xytedeviceget_config_0)
  * [`xyte.device.get_file`](#xytedeviceget_file)
  * [`xyte.device.get_files`](#xytedeviceget_files)
  * [`xyte.device.get_incidents`](#xytedeviceget_incidents)
  * [`xyte.device.get_info`](#xytedeviceget_info)
  * [`xyte.device.get_info_0`](#xytedeviceget_info_0)
  * [`xyte.device.get_license`](#xytedeviceget_license)
  * [`xyte.device.get_licenses`](#xytedeviceget_licenses)
  * [`xyte.device.get_space_info`](#xytedeviceget_space_info)
  * [`xyte.device.get_state_history`](#xytedeviceget_state_history)
  * [`xyte.device.get_telemetries`](#xytedeviceget_telemetries)
  * [`xyte.device.list_commands`](#xytedevicelist_commands)
  * [`xyte.device.list_devices`](#xytedevicelist_devices)
  * [`xyte.device.open_incident`](#xytedeviceopen_incident)
  * [`xyte.device.register_child_device`](#xytedeviceregister_child_device)
  * [`xyte.device.send_child_telemetries`](#xytedevicesend_child_telemetries)
  * [`xyte.device.send_command`](#xytedevicesend_command)
  * [`xyte.device.send_dump_file`](#xytedevicesend_dump_file)
  * [`xyte.device.send_telemetry`](#xytedevicesend_telemetry)
  * [`xyte.device.set_config`](#xytedeviceset_config)
  * [`xyte.device.update_cloud_settings`](#xytedeviceupdate_cloud_settings)
  * [`xyte.device.update_device`](#xytedeviceupdate_device)
  * [`xyte.device.update_license`](#xytedeviceupdate_license)
  * [`xyte.ticket.add_comment`](#xyteticketadd_comment)
  * [`xyte.ticket.close`](#xyteticketclose)
  * [`xyte.ticket.get_by_id`](#xyteticketget_by_id)
  * [`xyte.ticket.list`](#xyteticketlist)
  * [`xyte.ticket.update_ticket_by_id`](#xyteticketupdate_ticket_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Xyte&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from xyte_python_sdk import Xyte, ApiException

xyte = Xyte(
    sec0="YOUR_API_KEY",
)

try:
    # Append Dump File
    append_dump_file_response = xyte.device.append_dump_file(
        raw_body="string_example",
        device_id="deviceId_example",
        dump_id="dumpId_example",
    )
    print(append_dump_file_response)
except ApiException as e:
    print("Exception when calling DeviceApi.append_dump_file: %s\n" % e)
    pprint(e.body)
    if e.status == 401:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from xyte_python_sdk import Xyte, ApiException

xyte = Xyte(
    sec0="YOUR_API_KEY",
)


async def main():
    try:
        # Append Dump File
        append_dump_file_response = await xyte.device.aappend_dump_file(
            raw_body="string_example",
            device_id="deviceId_example",
            dump_id="dumpId_example",
        )
        print(append_dump_file_response)
    except ApiException as e:
        print("Exception when calling DeviceApi.append_dump_file: %s\n" % e)
        pprint(e.body)
        if e.status == 401:
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from xyte_python_sdk import Xyte, ApiException

xyte = Xyte(
    sec0="YOUR_API_KEY",
)

try:
    # Append Dump File
    append_dump_file_response = xyte.device.raw.append_dump_file(
        raw_body="string_example",
        device_id="deviceId_example",
        dump_id="dumpId_example",
    )
    pprint(append_dump_file_response.body)
    pprint(append_dump_file_response.body["length"])
    pprint(append_dump_file_response.headers)
    pprint(append_dump_file_response.status)
    pprint(append_dump_file_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DeviceApi.append_dump_file: %s\n" % e)
    pprint(e.body)
    if e.status == 401:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `xyte.device.append_dump_file`<a id="xytedeviceappend_dump_file"></a>

Append Dump File

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
append_dump_file_response = xyte.device.append_dump_file(
    raw_body="string_example",
    device_id="deviceId_example",
    dump_id="dumpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw_body: `str`<a id="raw_body-str"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### dump_id: `str`<a id="dump_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceAppendDumpFileRequest`](./xyte_python_sdk/type/device_append_dump_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceAppendDumpFileResponse`](./xyte_python_sdk/pydantic/device_append_dump_file_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/dumps/{dumpId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.close_incident`<a id="xytedeviceclose_incident"></a>

Close Incident

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
close_incident_response = xyte.device.close_incident(
    device_id="deviceId_example",
    incident_id="incidentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique Device ID

##### incident_id: `str`<a id="incident_id-str"></a>

The unique id of the incident to close

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceCloseIncidentResponse`](./xyte_python_sdk/pydantic/device_close_incident_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/incidents/{incidentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.create_registration`<a id="xytedevicecreate_registration"></a>

Register Device

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_registration_response = xyte.device.create_registration(
    sn="string_example",
    firmware_version="1.0.0",
    hardware_key="string_example",
    mac="string_example",
    cloud_id="string_example",
    name="string_example",
    details={},
    sub_model="string_example",
    parent_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sn: `str`<a id="sn-str"></a>

Unique device serial number

##### firmware_version: `str`<a id="firmware_version-str"></a>

Semver based firmware version

##### hardware_key: `str`<a id="hardware_key-str"></a>

Key defined in the model's hardware key section

##### mac: `str`<a id="mac-str"></a>

MAC address of the device

##### cloud_id: `str`<a id="cloud_id-str"></a>

Unique device identifier (must specify this or mac)

##### name: `str`<a id="name-str"></a>

Display name for the end-user

##### details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Generic JSON object with unconstrained data

##### sub_model: `str`<a id="sub_model-str"></a>

Additional model details text

##### parent_id: `str`<a id="parent_id-str"></a>

UUID of the parent device

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceCreateRegistrationRequest`](./xyte_python_sdk/type/device_create_registration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceCreateRegistrationResponse`](./xyte_python_sdk/pydantic/device_create_registration_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.delete_device`<a id="xytedevicedelete_device"></a>

Delete Device

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_device_response = xyte.device.delete_device(
    device_id="device_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's unique ID

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDeleteDeviceResponse`](./xyte_python_sdk/pydantic/device_delete_device_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/{device_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_all_device_state_histories`<a id="xytedeviceget_all_device_state_histories"></a>

Get All Device's State History

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_device_state_histories_response = xyte.device.get_all_device_state_histories(
    status="string_example",
    _from="beginning of current month",
    to="Current time",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Filter by state: online, offline, unavailable, error

##### _from: `datetime`<a id="_from-datetime"></a>

Query range

##### to: `datetime`<a id="to-datetime"></a>

Query range

##### page: `int`<a id="page-int"></a>

Pagination (500 records per page)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/histories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_child_devices`<a id="xytedeviceget_child_devices"></a>

Get Child Devices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_child_devices_response = xyte.device.get_child_devices(
    parent_id="parent_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent_id: `str`<a id="parent_id-str"></a>

The ID of the parent device

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetChildDevicesResponse`](./xyte_python_sdk/pydantic/device_get_child_devices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{parent_id}/children` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_command`<a id="xytedeviceget_command"></a>

Get Command

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_command_response = xyte.device.get_command(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/command` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_config`<a id="xytedeviceget_config"></a>

Get Config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_config_response = xyte.device.get_config(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetConfigResponse`](./xyte_python_sdk/pydantic/device_get_config_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/config` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_config_0`<a id="xytedeviceget_config_0"></a>

Get Device Configuration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_config_0_response = xyte.device.get_config_0(
    device_id="device_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique Device ID

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetConfig200Response`](./xyte_python_sdk/pydantic/device_get_config200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/{device_id}/config` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_file`<a id="xytedeviceget_file"></a>

Get File

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_response = xyte.device.get_file(
    device_id="deviceId_example",
    file_uuid="fileUuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### file_uuid: `str`<a id="file_uuid-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/files/{fileUuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_files`<a id="xytedeviceget_files"></a>

Get Files

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_files_response = xyte.device.get_files(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_incidents`<a id="xytedeviceget_incidents"></a>

Get Incidents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_incidents_response = xyte.device.get_incidents(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's unique ID

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetIncidentsResponse`](./xyte_python_sdk/pydantic/device_get_incidents_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/incidents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_info`<a id="xytedeviceget_info"></a>

Get Device Info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = xyte.device.get_info(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetInfoResponse`](./xyte_python_sdk/pydantic/device_get_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_info_0`<a id="xytedeviceget_info_0"></a>

Get Device Info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_0_response = xyte.device.get_info_0(
    device_id="device_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's unique ID

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetInfo200Response`](./xyte_python_sdk/pydantic/device_get_info200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/{device_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_license`<a id="xytedeviceget_license"></a>

Get License

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_license_response = xyte.device.get_license(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetLicenseResponse`](./xyte_python_sdk/pydantic/device_get_license_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/license` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_licenses`<a id="xytedeviceget_licenses"></a>

Get Licenses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_licenses_response = xyte.device.get_licenses(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetLicensesResponse`](./xyte_python_sdk/pydantic/device_get_licenses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/licenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_space_info`<a id="xytedeviceget_space_info"></a>

Get Space Info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_space_info_response = xyte.device.get_space_info(
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetSpaceInfoResponse`](./xyte_python_sdk/pydantic/device_get_space_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/space` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_state_history`<a id="xytedeviceget_state_history"></a>

Get Device State History

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_state_history_response = xyte.device.get_state_history(
    device_id="device_id_example",
    status="string_example",
    _from="beginning of current month",
    to="Current time",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique Device ID

##### status: `str`<a id="status-str"></a>

Filter by state: online, offline, unavailable, error

##### _from: `datetime`<a id="_from-datetime"></a>

Query range

##### to: `datetime`<a id="to-datetime"></a>

Query range

##### page: `int`<a id="page-int"></a>

Pagination (500 records per page)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/{device_id}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.get_telemetries`<a id="xytedeviceget_telemetries"></a>

Get Device Telemetries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_telemetries_response = xyte.device.get_telemetries(
    device_id="device_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique Device ID

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceGetTelemetriesResponse`](./xyte_python_sdk/pydantic/device_get_telemetries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/{device_id}/telemetries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.list_commands`<a id="xytedevicelist_commands"></a>

Get Device Commands

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_commands_response = xyte.device.list_commands(
    device_id="device_id_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique Device ID

##### status: `str`<a id="status-str"></a>

Filter by command status: scheduled, pending, done, failed, aborted, in_progress

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceListCommandsResponse`](./xyte_python_sdk/pydantic/device_list_commands_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices/{device_id}/commands` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.list_devices`<a id="xytedevicelist_devices"></a>

List Devices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_devices_response = xyte.device.list_devices(
    model_id="string_example",
    sn="string_example",
    mac="string_example",
    page="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model_id: `str`<a id="model_id-str"></a>

Filter by model id

##### sn: `str`<a id="sn-str"></a>

Filter by Serial Number

##### mac: `str`<a id="mac-str"></a>

Filter by MAC address

##### page: `str`<a id="page-str"></a>

Pagination selector

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceListDevicesResponse`](./xyte_python_sdk/pydantic/device_list_devices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/devices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.open_incident`<a id="xytedeviceopen_incident"></a>

Open Incident

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
open_incident_response = xyte.device.open_incident(
    title="string_example",
    device_id="deviceId_example",
    description="string_example",
    priority="3",
    issue="Randomly generated tag",
    raw_body="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Short title

##### device_id: `str`<a id="device_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### priority: `str`<a id="priority-str"></a>

Critical, High, Moderate, Low, Planning

##### issue: `str`<a id="issue-str"></a>

Short text to uniquely identify the issue (only one incident of each issue type can be open at a time)

##### raw_body: `str`<a id="raw_body-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceOpenIncidentRequest`](./xyte_python_sdk/type/device_open_incident_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceOpenIncidentResponse`](./xyte_python_sdk/pydantic/device_open_incident_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/incidents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.register_child_device`<a id="xytedeviceregister_child_device"></a>

Register Child Device

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_child_device_response = xyte.device.register_child_device(
    firmware_version="string_example",
    model_id="string_example",
    parent_id="parent_id_example",
    sub_model="string_example",
    sn="string_example",
    mac="string_example",
    name="string_example",
    details={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### firmware_version: `str`<a id="firmware_version-str"></a>

##### model_id: `str`<a id="model_id-str"></a>

##### parent_id: `str`<a id="parent_id-str"></a>

The ID of the parent device

##### sub_model: `str`<a id="sub_model-str"></a>

##### sn: `str`<a id="sn-str"></a>

##### mac: `str`<a id="mac-str"></a>

##### name: `str`<a id="name-str"></a>

##### details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceRegisterChildDeviceRequest`](./xyte_python_sdk/type/device_register_child_device_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceRegisterChildDeviceResponse`](./xyte_python_sdk/pydantic/device_register_child_device_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{parent_id}/children` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.send_child_telemetries`<a id="xytedevicesend_child_telemetries"></a>

Send Child Telemetries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_child_telemetries_response = xyte.device.send_child_telemetries(
    raw_body={},
    device_id="deviceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw_body: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="raw_body-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Mapping of child device UUIDs to telemetry data for each device

##### device_id: `str`<a id="device_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceSendChildTelemetriesRequest`](./xyte_python_sdk/type/device_send_child_telemetries_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceSendChildTelemetriesResponse`](./xyte_python_sdk/pydantic/device_send_child_telemetries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/children/telemetries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.send_command`<a id="xytedevicesend_command"></a>

Update Command

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_command_response = xyte.device.send_command(
    status="done",
    id="string_example",
    device_id="deviceId_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### id: `str`<a id="id-str"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### message: `str`<a id="message-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceSendCommandRequest`](./xyte_python_sdk/type/device_send_command_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceSendCommandResponse`](./xyte_python_sdk/pydantic/device_send_command_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/command` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.send_dump_file`<a id="xytedevicesend_dump_file"></a>

Send Dump

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_dump_file_response = xyte.device.send_dump_file(
    raw_body=open("/path/to/file", "rb"),
    device_id="deviceId_example",
    mime_type="text/plain",
    filename="filename",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw_body: `IO`<a id="raw_body-io"></a>

Raw configuration dump

##### device_id: `str`<a id="device_id-str"></a>

##### mime_type: `str`<a id="mime_type-str"></a>

##### filename: `str`<a id="filename-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceSendDumpFileRequest`](./xyte_python_sdk/type/device_send_dump_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceSendDumpFileResponse`](./xyte_python_sdk/pydantic/device_send_dump_file_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/dumps/{mime-type}/{filename}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.send_telemetry`<a id="xytedevicesend_telemetry"></a>

Send Telemetry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_telemetry_response = xyte.device.send_telemetry(
    status="online",
    device_id="deviceId_example",
    timestamp="1970-01-01",
    telemetries="string_example",
    override=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### timestamp: `date`<a id="timestamp-date"></a>

##### telemetries: `str`<a id="telemetries-str"></a>

##### override: `bool`<a id="override-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceSendTelemetryRequest`](./xyte_python_sdk/type/device_send_telemetry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceSendTelemetryResponse`](./xyte_python_sdk/pydantic/device_send_telemetry_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/telemetry` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.set_config`<a id="xytedeviceset_config"></a>

Set Config

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_config_response = xyte.device.set_config(
    device_id="deviceId_example",
    raw_body="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### raw_body: `str`<a id="raw_body-str"></a>

Put your raw JSON config here

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceSetConfigRequest`](./xyte_python_sdk/type/device_set_config_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceSetConfigResponse`](./xyte_python_sdk/pydantic/device_set_config_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/config` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.update_cloud_settings`<a id="xytedeviceupdate_cloud_settings"></a>

Set Cloud Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_cloud_settings_response = xyte.device.update_cloud_settings(
    device_id="deviceId_example",
    _property="string_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### _property: `str`<a id="_property-str"></a>

The Property you would like to change

##### value: `str`<a id="value-str"></a>

The value to set for the given propery

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceUpdateCloudSettingsRequest`](./xyte_python_sdk/type/device_update_cloud_settings_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/cloud_settings` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.update_device`<a id="xytedeviceupdate_device"></a>

Update Device

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_device_response = xyte.device.update_device(
    device_id="deviceId_example",
    firmware_version="string_example",
    name="string_example",
    space_version="string_example",
    config_version="string_example",
    details={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### firmware_version: `str`<a id="firmware_version-str"></a>

##### name: `str`<a id="name-str"></a>

Friendly device name

##### space_version: `str`<a id="space_version-str"></a>

Latest version of the space information the device has applied

##### config_version: `str`<a id="config_version-str"></a>

Latest version of the configuration the device has applied

##### details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Details of the device. Will be visible in a different tab on the device's view calls 'Details'.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceUpdateDeviceRequest`](./xyte_python_sdk/type/device_update_device_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceUpdateDeviceResponse`](./xyte_python_sdk/pydantic/device_update_device_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.device.update_license`<a id="xytedeviceupdate_license"></a>

Update License

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_license_response = xyte.device.update_license(
    id="string_example",
    state="string_example",
    device_id="deviceId_example",
    error="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### state: `str`<a id="state-str"></a>

##### device_id: `str`<a id="device_id-str"></a>

##### error: `str`<a id="error-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceUpdateLicenseRequest`](./xyte_python_sdk/type/device_update_license_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceUpdateLicenseResponse`](./xyte_python_sdk/pydantic/device_update_license_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/devices/{deviceId}/licenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.ticket.add_comment`<a id="xyteticketadd_comment"></a>

Add Comment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_comment_response = xyte.ticket.add_comment(
    ticket_id="ticket_id_example",
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ticket_id: `str`<a id="ticket_id-str"></a>

Unique ticket ID

##### message: `str`<a id="message-str"></a>

Message to post

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TicketAddCommentRequest`](./xyte_python_sdk/type/ticket_add_comment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TicketAddCommentResponse`](./xyte_python_sdk/pydantic/ticket_add_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/tickets/{ticket_id}/message` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.ticket.close`<a id="xyteticketclose"></a>

Close Ticket

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
close_response = xyte.ticket.close(
    ticket_id="ticket_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ticket_id: `str`<a id="ticket_id-str"></a>

Unique ticket ID

#### 🔄 Return<a id="🔄-return"></a>

[`TicketCloseResponse`](./xyte_python_sdk/pydantic/ticket_close_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/tickets/{ticket_id}/resolved` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.ticket.get_by_id`<a id="xyteticketget_by_id"></a>

Get Ticket

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = xyte.ticket.get_by_id(
    ticket_id="ticket_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ticket_id: `str`<a id="ticket_id-str"></a>

Unique ticket ID

#### 🔄 Return<a id="🔄-return"></a>

[`TicketGetByIdResponse`](./xyte_python_sdk/pydantic/ticket_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/tickets/{ticket_id} (COPY)` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.ticket.list`<a id="xyteticketlist"></a>

List Tickets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = xyte.ticket.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TicketListResponse`](./xyte_python_sdk/pydantic/ticket_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/tickets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `xyte.ticket.update_ticket_by_id`<a id="xyteticketupdate_ticket_by_id"></a>

Update Ticket

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_ticket_by_id_response = xyte.ticket.update_ticket_by_id(
    ticket_id="ticket_id_example",
    title="string_example",
    description="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ticket_id: `str`<a id="ticket_id-str"></a>

Unique ticket ID

##### title: `str`<a id="title-str"></a>

New ticket title

##### description: `str`<a id="description-str"></a>

New ticket description

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TicketUpdateTicketByIdRequest`](./xyte_python_sdk/type/ticket_update_ticket_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TicketUpdateTicketByIdResponse`](./xyte_python_sdk/pydantic/ticket_update_ticket_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/partner/tickets/{ticket_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)

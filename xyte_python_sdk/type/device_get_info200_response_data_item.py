# coding: utf-8

"""
    Testing API

    Xyte's Device Cloud is the first all-in-one servitization platform designed for device and hardware manufacturers to cloudify, operate, support, and commercialize their connected devices in a unified platform.   We enable OEMs across different industries to navigate their digital journey, transforming their devices into integrated business solutions that combine hardware, software and services. The only business and commerce platform designed specifically for IoT device manufacturers, our fully-federated Device Cloud empowers OEMs to manage the complete lifecycle of their devices, from the minute they leave the warehouse through aftermarket sales to end customers.  Our out-of-the-box applications for asset management, remote support, ecommerce and subscription management, financing, and a powerful and secure back office suite help OEMs boost revenue and market growth, optimize operational efficiencies, gain instant insights into equipment and device performance, and develop sustainable customer relationships.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from xyte_python_sdk.type.device_get_info200_response_data_item_firmware import DeviceGetInfo200ResponseDataItemFirmware
from xyte_python_sdk.type.device_get_info200_response_data_item_model import DeviceGetInfo200ResponseDataItemModel

class RequiredDeviceGetInfo200ResponseDataItem(TypedDict):
    pass

class OptionalDeviceGetInfo200ResponseDataItem(TypedDict, total=False):
    id: str

    sn: str

    mac: str

    cloud_id: str

    status: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    last_seen_at: str

    details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    state: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    model: DeviceGetInfo200ResponseDataItemModel

    firmware: DeviceGetInfo200ResponseDataItemFirmware

class DeviceGetInfo200ResponseDataItem(RequiredDeviceGetInfo200ResponseDataItem, OptionalDeviceGetInfo200ResponseDataItem):
    pass

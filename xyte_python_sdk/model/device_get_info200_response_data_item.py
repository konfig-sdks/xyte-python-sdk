# coding: utf-8

"""
    Testing API

    Xyte's Device Cloud is the first all-in-one servitization platform designed for device and hardware manufacturers to cloudify, operate, support, and commercialize their connected devices in a unified platform.   We enable OEMs across different industries to navigate their digital journey, transforming their devices into integrated business solutions that combine hardware, software and services. The only business and commerce platform designed specifically for IoT device manufacturers, our fully-federated Device Cloud empowers OEMs to manage the complete lifecycle of their devices, from the minute they leave the warehouse through aftermarket sales to end customers.  Our out-of-the-box applications for asset management, remote support, ecommerce and subscription management, financing, and a powerful and secure back office suite help OEMs boost revenue and market growth, optimize operational efficiencies, gain instant insights into equipment and device performance, and develop sustainable customer relationships.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from xyte_python_sdk import schemas  # noqa: F401


class DeviceGetInfo200ResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            sn = schemas.StrSchema
            mac = schemas.StrSchema
            cloud_id = schemas.StrSchema
            status = schemas.AnyTypeSchema
            last_seen_at = schemas.StrSchema
            details = schemas.DictSchema
            state = schemas.DictSchema
        
            @staticmethod
            def model() -> typing.Type['DeviceGetInfo200ResponseDataItemModel']:
                return DeviceGetInfo200ResponseDataItemModel
        
            @staticmethod
            def firmware() -> typing.Type['DeviceGetInfo200ResponseDataItemFirmware']:
                return DeviceGetInfo200ResponseDataItemFirmware
            __annotations__ = {
                "id": id,
                "sn": sn,
                "mac": mac,
                "cloud_id": cloud_id,
                "status": status,
                "last_seen_at": last_seen_at,
                "details": details,
                "state": state,
                "model": model,
                "firmware": firmware,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sn"]) -> MetaOapg.properties.sn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac"]) -> MetaOapg.properties.mac: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloud_id"]) -> MetaOapg.properties.cloud_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> 'DeviceGetInfo200ResponseDataItemModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware"]) -> 'DeviceGetInfo200ResponseDataItemFirmware': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sn", "mac", "cloud_id", "status", "last_seen_at", "details", "state", "model", "firmware", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sn"]) -> typing.Union[MetaOapg.properties.sn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac"]) -> typing.Union[MetaOapg.properties.mac, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloud_id"]) -> typing.Union[MetaOapg.properties.cloud_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_seen_at"]) -> typing.Union[MetaOapg.properties.last_seen_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> typing.Union['DeviceGetInfo200ResponseDataItemModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware"]) -> typing.Union['DeviceGetInfo200ResponseDataItemFirmware', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sn", "mac", "cloud_id", "status", "last_seen_at", "details", "state", "model", "firmware", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        sn: typing.Union[MetaOapg.properties.sn, str, schemas.Unset] = schemas.unset,
        mac: typing.Union[MetaOapg.properties.mac, str, schemas.Unset] = schemas.unset,
        cloud_id: typing.Union[MetaOapg.properties.cloud_id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        last_seen_at: typing.Union[MetaOapg.properties.last_seen_at, str, schemas.Unset] = schemas.unset,
        details: typing.Union[MetaOapg.properties.details, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        model: typing.Union['DeviceGetInfo200ResponseDataItemModel', schemas.Unset] = schemas.unset,
        firmware: typing.Union['DeviceGetInfo200ResponseDataItemFirmware', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceGetInfo200ResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            sn=sn,
            mac=mac,
            cloud_id=cloud_id,
            status=status,
            last_seen_at=last_seen_at,
            details=details,
            state=state,
            model=model,
            firmware=firmware,
            _configuration=_configuration,
            **kwargs,
        )

from xyte_python_sdk.model.device_get_info200_response_data_item_firmware import DeviceGetInfo200ResponseDataItemFirmware
from xyte_python_sdk.model.device_get_info200_response_data_item_model import DeviceGetInfo200ResponseDataItemModel

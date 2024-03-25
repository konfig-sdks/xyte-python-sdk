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


class DeviceGetInfoResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def partner() -> typing.Type['DeviceGetInfoResponsePartner']:
                return DeviceGetInfoResponsePartner
        
            @staticmethod
            def config() -> typing.Type['DeviceGetInfoResponseConfig']:
                return DeviceGetInfoResponseConfig
        
            @staticmethod
            def state() -> typing.Type['DeviceGetInfoResponseState']:
                return DeviceGetInfoResponseState
            last_seen = schemas.StrSchema
        
            @staticmethod
            def custom() -> typing.Type['DeviceGetInfoResponseCustom']:
                return DeviceGetInfoResponseCustom
            name = schemas.StrSchema
            firmware_version = schemas.StrSchema
            claimed = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "partner": partner,
                "config": config,
                "state": state,
                "last_seen": last_seen,
                "custom": custom,
                "name": name,
                "firmware_version": firmware_version,
                "claimed": claimed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partner"]) -> 'DeviceGetInfoResponsePartner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> 'DeviceGetInfoResponseConfig': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'DeviceGetInfoResponseState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_seen"]) -> MetaOapg.properties.last_seen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> 'DeviceGetInfoResponseCustom': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware_version"]) -> MetaOapg.properties.firmware_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claimed"]) -> MetaOapg.properties.claimed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "partner", "config", "state", "last_seen", "custom", "name", "firmware_version", "claimed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partner"]) -> typing.Union['DeviceGetInfoResponsePartner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union['DeviceGetInfoResponseConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union['DeviceGetInfoResponseState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_seen"]) -> typing.Union[MetaOapg.properties.last_seen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union['DeviceGetInfoResponseCustom', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware_version"]) -> typing.Union[MetaOapg.properties.firmware_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claimed"]) -> typing.Union[MetaOapg.properties.claimed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "partner", "config", "state", "last_seen", "custom", "name", "firmware_version", "claimed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partner: typing.Union['DeviceGetInfoResponsePartner', schemas.Unset] = schemas.unset,
        config: typing.Union['DeviceGetInfoResponseConfig', schemas.Unset] = schemas.unset,
        state: typing.Union['DeviceGetInfoResponseState', schemas.Unset] = schemas.unset,
        last_seen: typing.Union[MetaOapg.properties.last_seen, str, schemas.Unset] = schemas.unset,
        custom: typing.Union['DeviceGetInfoResponseCustom', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        firmware_version: typing.Union[MetaOapg.properties.firmware_version, str, schemas.Unset] = schemas.unset,
        claimed: typing.Union[MetaOapg.properties.claimed, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceGetInfoResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            partner=partner,
            config=config,
            state=state,
            last_seen=last_seen,
            custom=custom,
            name=name,
            firmware_version=firmware_version,
            claimed=claimed,
            _configuration=_configuration,
            **kwargs,
        )

from xyte_python_sdk.model.device_get_info_response_config import DeviceGetInfoResponseConfig
from xyte_python_sdk.model.device_get_info_response_custom import DeviceGetInfoResponseCustom
from xyte_python_sdk.model.device_get_info_response_partner import DeviceGetInfoResponsePartner
from xyte_python_sdk.model.device_get_info_response_state import DeviceGetInfoResponseState

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


class TicketCloseResponseCommentsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            text = schemas.StrSchema
            created_at = schemas.StrSchema
            system = schemas.BoolSchema
            user = schemas.StrSchema
            owner = schemas.StrSchema
            owner_type = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "text": text,
                "created_at": created_at,
                "system": system,
                "user": user,
                "owner": owner,
                "owner_type": owner_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_type"]) -> MetaOapg.properties.owner_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "text", "created_at", "system", "user", "owner", "owner_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> typing.Union[MetaOapg.properties.system, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_type"]) -> typing.Union[MetaOapg.properties.owner_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "text", "created_at", "system", "user", "owner", "owner_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        system: typing.Union[MetaOapg.properties.system, bool, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
        owner_type: typing.Union[MetaOapg.properties.owner_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TicketCloseResponseCommentsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            text=text,
            created_at=created_at,
            system=system,
            user=user,
            owner=owner,
            owner_type=owner_type,
            _configuration=_configuration,
            **kwargs,
        )

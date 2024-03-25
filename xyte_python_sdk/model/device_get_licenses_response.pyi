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


class DeviceGetLicensesResponse(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                
                
                class items(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        
                        class properties:
                            data = schemas.StrSchema
                            signature = schemas.StrSchema
                            id = schemas.StrSchema
                            add = schemas.BoolSchema
                            __annotations__ = {
                                "data": data,
                                "signature": signature,
                                "id": id,
                                "add": add,
                            }
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["add"]) -> MetaOapg.properties.add: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "signature", "id", "add", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> typing.Union[MetaOapg.properties.signature, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["add"]) -> typing.Union[MetaOapg.properties.add, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "signature", "id", "add", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        data: typing.Union[MetaOapg.properties.data, str, schemas.Unset] = schemas.unset,
                        signature: typing.Union[MetaOapg.properties.signature, str, schemas.Unset] = schemas.unset,
                        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                        add: typing.Union[MetaOapg.properties.add, bool, schemas.Unset] = schemas.unset,
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'items':
                        return super().__new__(
                            cls,
                            *args,
                            data=data,
                            signature=signature,
                            id=id,
                            add=add,
                            _configuration=_configuration,
                            **kwargs,
                        )
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)
        
        
        class one_of_1(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                items = schemas.AnyTypeSchema
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceGetLicensesResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

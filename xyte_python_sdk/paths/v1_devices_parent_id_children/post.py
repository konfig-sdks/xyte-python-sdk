# coding: utf-8

"""
    Testing API

    Xyte's Device Cloud is the first all-in-one servitization platform designed for device and hardware manufacturers to cloudify, operate, support, and commercialize their connected devices in a unified platform.   We enable OEMs across different industries to navigate their digital journey, transforming their devices into integrated business solutions that combine hardware, software and services. The only business and commerce platform designed specifically for IoT device manufacturers, our fully-federated Device Cloud empowers OEMs to manage the complete lifecycle of their devices, from the minute they leave the warehouse through aftermarket sales to end customers.  Our out-of-the-box applications for asset management, remote support, ecommerce and subscription management, financing, and a powerful and secure back office suite help OEMs boost revenue and market growth, optimize operational efficiencies, gain instant insights into equipment and device performance, and develop sustainable customer relationships.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from xyte_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from xyte_python_sdk.api_response import AsyncGeneratorResponse
from xyte_python_sdk import api_client, exceptions
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

from xyte_python_sdk.model.device_register_child_device_request import DeviceRegisterChildDeviceRequest as DeviceRegisterChildDeviceRequestSchema
from xyte_python_sdk.model.device_register_child_device_response import DeviceRegisterChildDeviceResponse as DeviceRegisterChildDeviceResponseSchema
from xyte_python_sdk.model.device_register_child_device404_response import DeviceRegisterChildDevice404Response as DeviceRegisterChildDevice404ResponseSchema
from xyte_python_sdk.model.device_register_child_device401_response import DeviceRegisterChildDevice401Response as DeviceRegisterChildDevice401ResponseSchema

from xyte_python_sdk.type.device_register_child_device401_response import DeviceRegisterChildDevice401Response
from xyte_python_sdk.type.device_register_child_device404_response import DeviceRegisterChildDevice404Response
from xyte_python_sdk.type.device_register_child_device_response import DeviceRegisterChildDeviceResponse
from xyte_python_sdk.type.device_register_child_device_request import DeviceRegisterChildDeviceRequest

from ...api_client import Dictionary
from xyte_python_sdk.pydantic.device_register_child_device404_response import DeviceRegisterChildDevice404Response as DeviceRegisterChildDevice404ResponsePydantic
from xyte_python_sdk.pydantic.device_register_child_device_request import DeviceRegisterChildDeviceRequest as DeviceRegisterChildDeviceRequestPydantic
from xyte_python_sdk.pydantic.device_register_child_device401_response import DeviceRegisterChildDevice401Response as DeviceRegisterChildDevice401ResponsePydantic
from xyte_python_sdk.pydantic.device_register_child_device_response import DeviceRegisterChildDeviceResponse as DeviceRegisterChildDeviceResponsePydantic

from . import path

# Path params
ParentIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'parent_id': typing.Union[ParentIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_parent_id = api_client.PathParameter(
    name="parent_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ParentIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = DeviceRegisterChildDeviceRequestSchema


request_body_device_register_child_device_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor201ResponseBodyApplicationJson = DeviceRegisterChildDeviceResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: DeviceRegisterChildDeviceResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: DeviceRegisterChildDeviceResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = DeviceRegisterChildDevice401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: DeviceRegisterChildDevice401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: DeviceRegisterChildDevice401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyTextPlain = DeviceRegisterChildDevice404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: DeviceRegisterChildDevice404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: DeviceRegisterChildDevice404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextPlain),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _register_child_device_mapped_args(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if firmware_version is not None:
            _body["firmware_version"] = firmware_version
        if model_id is not None:
            _body["model_id"] = model_id
        if sub_model is not None:
            _body["sub_model"] = sub_model
        if sn is not None:
            _body["sn"] = sn
        if mac is not None:
            _body["mac"] = mac
        if name is not None:
            _body["name"] = name
        if details is not None:
            _body["details"] = details
        args.body = _body
        if parent_id is not None:
            _path_params["parent_id"] = parent_id
        args.path = _path_params
        return args

    async def _aregister_child_device_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Register Child Device
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_parent_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/devices/{parent_id}/children',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_device_register_child_device_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _register_child_device_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Register Child Device
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_parent_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/devices/{parent_id}/children',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_device_register_child_device_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class RegisterChildDeviceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aregister_child_device(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._register_child_device_mapped_args(
            firmware_version=firmware_version,
            model_id=model_id,
            parent_id=parent_id,
            sub_model=sub_model,
            sn=sn,
            mac=mac,
            name=name,
            details=details,
        )
        return await self._aregister_child_device_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def register_child_device(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._register_child_device_mapped_args(
            firmware_version=firmware_version,
            model_id=model_id,
            parent_id=parent_id,
            sub_model=sub_model,
            sn=sn,
            mac=mac,
            name=name,
            details=details,
        )
        return self._register_child_device_oapg(
            body=args.body,
            path_params=args.path,
        )

class RegisterChildDevice(BaseApi):

    async def aregister_child_device(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> DeviceRegisterChildDeviceResponsePydantic:
        raw_response = await self.raw.aregister_child_device(
            firmware_version=firmware_version,
            model_id=model_id,
            parent_id=parent_id,
            sub_model=sub_model,
            sn=sn,
            mac=mac,
            name=name,
            details=details,
            **kwargs,
        )
        if validate:
            return DeviceRegisterChildDeviceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DeviceRegisterChildDeviceResponsePydantic, raw_response.body)
    
    
    def register_child_device(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> DeviceRegisterChildDeviceResponsePydantic:
        raw_response = self.raw.register_child_device(
            firmware_version=firmware_version,
            model_id=model_id,
            parent_id=parent_id,
            sub_model=sub_model,
            sn=sn,
            mac=mac,
            name=name,
            details=details,
        )
        if validate:
            return DeviceRegisterChildDeviceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DeviceRegisterChildDeviceResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._register_child_device_mapped_args(
            firmware_version=firmware_version,
            model_id=model_id,
            parent_id=parent_id,
            sub_model=sub_model,
            sn=sn,
            mac=mac,
            name=name,
            details=details,
        )
        return await self._aregister_child_device_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        firmware_version: str,
        model_id: str,
        parent_id: str,
        sub_model: typing.Optional[str] = None,
        sn: typing.Optional[str] = None,
        mac: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._register_child_device_mapped_args(
            firmware_version=firmware_version,
            model_id=model_id,
            parent_id=parent_id,
            sub_model=sub_model,
            sn=sn,
            mac=mac,
            name=name,
            details=details,
        )
        return self._register_child_device_oapg(
            body=args.body,
            path_params=args.path,
        )


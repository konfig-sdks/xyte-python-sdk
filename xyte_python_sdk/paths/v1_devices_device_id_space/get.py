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

from xyte_python_sdk.model.device_get_space_info_response import DeviceGetSpaceInfoResponse as DeviceGetSpaceInfoResponseSchema
from xyte_python_sdk.model.device_get_space_info422_response import DeviceGetSpaceInfo422Response as DeviceGetSpaceInfo422ResponseSchema

from xyte_python_sdk.type.device_get_space_info422_response import DeviceGetSpaceInfo422Response
from xyte_python_sdk.type.device_get_space_info_response import DeviceGetSpaceInfoResponse

from ...api_client import Dictionary
from xyte_python_sdk.pydantic.device_get_space_info422_response import DeviceGetSpaceInfo422Response as DeviceGetSpaceInfo422ResponsePydantic
from xyte_python_sdk.pydantic.device_get_space_info_response import DeviceGetSpaceInfoResponse as DeviceGetSpaceInfoResponsePydantic

from . import path

# Path params
DeviceIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'deviceId': typing.Union[DeviceIdSchema, str, ],
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


request_path_device_id = api_client.PathParameter(
    name="deviceId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DeviceIdSchema,
    required=True,
)
_auth = [
    'sec0',
]
SchemaFor201ResponseBodyApplicationJson = DeviceGetSpaceInfoResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: DeviceGetSpaceInfoResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: DeviceGetSpaceInfoResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = DeviceGetSpaceInfo422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: DeviceGetSpaceInfo422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: DeviceGetSpaceInfo422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_space_info_mapped_args(
        self,
        device_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if device_id is not None:
            _path_params["deviceId"] = device_id
        args.path = _path_params
        return args

    async def _aget_space_info_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Space Info
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_device_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/devices/{deviceId}/space',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_space_info_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Space Info
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_device_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/devices/{deviceId}/space',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetSpaceInfoRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_space_info(
        self,
        device_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_space_info_mapped_args(
            device_id=device_id,
        )
        return await self._aget_space_info_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_space_info(
        self,
        device_id: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_space_info_mapped_args(
            device_id=device_id,
        )
        return self._get_space_info_oapg(
            path_params=args.path,
        )

class GetSpaceInfo(BaseApi):

    async def aget_space_info(
        self,
        device_id: str,
        validate: bool = False,
        **kwargs,
    ) -> DeviceGetSpaceInfoResponsePydantic:
        raw_response = await self.raw.aget_space_info(
            device_id=device_id,
            **kwargs,
        )
        if validate:
            return DeviceGetSpaceInfoResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DeviceGetSpaceInfoResponsePydantic, raw_response.body)
    
    
    def get_space_info(
        self,
        device_id: str,
        validate: bool = False,
    ) -> DeviceGetSpaceInfoResponsePydantic:
        raw_response = self.raw.get_space_info(
            device_id=device_id,
        )
        if validate:
            return DeviceGetSpaceInfoResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DeviceGetSpaceInfoResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        device_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_space_info_mapped_args(
            device_id=device_id,
        )
        return await self._aget_space_info_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        device_id: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_space_info_mapped_args(
            device_id=device_id,
        )
        return self._get_space_info_oapg(
            path_params=args.path,
        )


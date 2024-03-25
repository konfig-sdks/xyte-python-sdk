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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from xyte_python_sdk.pydantic.ticket_close_response_comments import TicketCloseResponseComments

class TicketCloseResponse(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    status: typing.Optional[str] = Field(None, alias='status')

    created_at: typing.Optional[str] = Field(None, alias='created_at')

    device_id: typing.Optional[str] = Field(None, alias='device_id')

    user_name: typing.Optional[str] = Field(None, alias='user_name')

    user_email: typing.Optional[str] = Field(None, alias='user_email')

    comments: typing.Optional[TicketCloseResponseComments] = Field(None, alias='comments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

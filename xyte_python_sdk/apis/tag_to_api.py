import typing_extensions

from xyte_python_sdk.apis.tags import TagValues
from xyte_python_sdk.apis.tags.device_api import DeviceApi
from xyte_python_sdk.apis.tags.ticket_api import TicketApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEVICE: DeviceApi,
        TagValues.TICKET: TicketApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEVICE: DeviceApi,
        TagValues.TICKET: TicketApi,
    }
)

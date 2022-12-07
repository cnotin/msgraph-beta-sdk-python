from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

accept_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.accept.accept_request_builder')
attachments_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.attachments.attachments_request_builder')
attachment_item_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.attachments.item.attachment_item_request_builder')
calendar_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.calendar.calendar_request_builder')
cancel_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.cancel.cancel_request_builder')
decline_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.decline.decline_request_builder')
dismiss_reminder_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.dismiss_reminder.dismiss_reminder_request_builder')
exception_occurrences_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.exception_occurrences.exception_occurrences_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.exception_occurrences.item.event_item_request_builder')
extensions_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.extensions.extensions_request_builder')
extension_item_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.extensions.item.extension_item_request_builder')
forward_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.forward.forward_request_builder')
instances_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.instances.instances_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.instances.item.event_item_request_builder')
multi_value_extended_properties_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.multi_value_extended_properties.multi_value_extended_properties_request_builder')
multi_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.multi_value_extended_properties.item.multi_value_legacy_extended_property_item_request_builder')
single_value_extended_properties_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.single_value_extended_properties.single_value_extended_properties_request_builder')
single_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.single_value_extended_properties.item.single_value_legacy_extended_property_item_request_builder')
snooze_reminder_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.snooze_reminder.snooze_reminder_request_builder')
tentatively_accept_request_builder = lazy_import('msgraph.generated.me.calendar_view.item.tentatively_accept.tentatively_accept_request_builder')
event = lazy_import('msgraph.generated.models.event')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class EventItemRequestBuilder():
    """
    Provides operations to manage the calendarView property of the microsoft.graph.user entity.
    """
    def accept(self) -> accept_request_builder.AcceptRequestBuilder:
        """
        Provides operations to call the accept method.
        """
        return accept_request_builder.AcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attachments(self) -> attachments_request_builder.AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.event entity.
        """
        return attachments_request_builder.AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.event entity.
        """
        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    def cancel(self) -> cancel_request_builder.CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        return cancel_request_builder.CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    def decline(self) -> decline_request_builder.DeclineRequestBuilder:
        """
        Provides operations to call the decline method.
        """
        return decline_request_builder.DeclineRequestBuilder(self.request_adapter, self.path_parameters)
    
    def dismiss_reminder(self) -> dismiss_reminder_request_builder.DismissReminderRequestBuilder:
        """
        Provides operations to call the dismissReminder method.
        """
        return dismiss_reminder_request_builder.DismissReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    def exception_occurrences(self) -> exception_occurrences_request_builder.ExceptionOccurrencesRequestBuilder:
        """
        Provides operations to manage the exceptionOccurrences property of the microsoft.graph.event entity.
        """
        return exception_occurrences_request_builder.ExceptionOccurrencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.event entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def forward(self) -> forward_request_builder.ForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        return forward_request_builder.ForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    def instances(self) -> instances_request_builder.InstancesRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.event entity.
        """
        return instances_request_builder.InstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.event entity.
        """
        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.event entity.
        """
        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def snooze_reminder(self) -> snooze_reminder_request_builder.SnoozeReminderRequestBuilder:
        """
        Provides operations to call the snoozeReminder method.
        """
        return snooze_reminder_request_builder.SnoozeReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    def tentatively_accept(self) -> tentatively_accept_request_builder.TentativelyAcceptRequestBuilder:
        """
        Provides operations to call the tentativelyAccept method.
        """
        return tentatively_accept_request_builder.TentativelyAcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attachments_by_id(self,id: str) -> attachment_item_request_builder.AttachmentItemRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: attachment_item_request_builder.AttachmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachment%2Did"] = id
        return attachment_item_request_builder.AttachmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EventItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/calendarView/{event%2Did}{?startDateTime*,endDateTime*,%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The calendar view for the calendar. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def exception_occurrences_by_id(self,id: str) -> EventItemRequestBuilder:
        """
        Provides operations to manage the exceptionOccurrences property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did1"] = id
        return EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[event.Event]:
        """
        The calendar view for the calendar. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[event.Event]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, event.Event, response_handler, error_mapping)
    
    def instances_by_id(self,id: str) -> EventItemRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did1"] = id
        return EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def multi_value_extended_properties_by_id(self,id: str) -> multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiValueLegacyExtendedProperty%2Did"] = id
        return multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def single_value_extended_properties_by_id(self,id: str) -> single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["singleValueLegacyExtendedProperty%2Did"] = id
        return single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class EventItemRequestBuilderGetQueryParameters():
        """
        The calendar view for the calendar. Read-only. Nullable.
        """
        # The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
        end_date_time: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
        start_date_time: Optional[str] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class EventItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EventItemRequestBuilder.EventItemRequestBuilderGetQueryParameters] = None

    


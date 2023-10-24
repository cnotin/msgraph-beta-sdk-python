from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.user_settings import UserSettings
    from .contact_merge_suggestions.contact_merge_suggestions_request_builder import ContactMergeSuggestionsRequestBuilder
    from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder
    from .regional_and_language_settings.regional_and_language_settings_request_builder import RegionalAndLanguageSettingsRequestBuilder
    from .shift_preferences.shift_preferences_request_builder import ShiftPreferencesRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the settings property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/settings{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property settings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[UserSettings]:
        """
        Get settings from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.user_settings import UserSettings

        return await self.request_adapter.send_async(request_info, UserSettings, error_mapping)
    
    async def patch(self,body: Optional[UserSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> Optional[UserSettings]:
        """
        Update the navigation property settings in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserSettings]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.user_settings import UserSettings

        return await self.request_adapter.send_async(request_info, UserSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property settings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.try_add_request_header("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get settings from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.try_add_request_header("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[UserSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property settings in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.try_add_request_header("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def contact_merge_suggestions(self) -> ContactMergeSuggestionsRequestBuilder:
        """
        Provides operations to manage the contactMergeSuggestions property of the microsoft.graph.userSettings entity.
        """
        from .contact_merge_suggestions.contact_merge_suggestions_request_builder import ContactMergeSuggestionsRequestBuilder

        return ContactMergeSuggestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_insights(self) -> ItemInsightsRequestBuilder:
        """
        Provides operations to manage the itemInsights property of the microsoft.graph.userSettings entity.
        """
        from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder

        return ItemInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def regional_and_language_settings(self) -> RegionalAndLanguageSettingsRequestBuilder:
        """
        Provides operations to manage the regionalAndLanguageSettings property of the microsoft.graph.userSettings entity.
        """
        from .regional_and_language_settings.regional_and_language_settings_request_builder import RegionalAndLanguageSettingsRequestBuilder

        return RegionalAndLanguageSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shift_preferences(self) -> ShiftPreferencesRequestBuilder:
        """
        Provides operations to manage the shiftPreferences property of the microsoft.graph.userSettings entity.
        """
        from .shift_preferences.shift_preferences_request_builder import ShiftPreferencesRequestBuilder

        return ShiftPreferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Get settings from users
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SettingsRequestBuilder.SettingsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    


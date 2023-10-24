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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.security.whois_record import WhoisRecord
    from .history.history_request_builder import HistoryRequestBuilder
    from .host.host_request_builder import HostRequestBuilder

class WhoisRecordItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the whoisRecords property of the microsoft.graph.security.threatIntelligence entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WhoisRecordItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/whoisRecords/{whoisRecord%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[WhoisRecordItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property whoisRecords for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WhoisRecordItemRequestBuilderGetRequestConfiguration] = None) -> Optional[WhoisRecord]:
        """
        Get the specified whoisRecord resource.  Specify the desired whoisRecord in one of the following two ways:- Identify a host and get its current whoisRecord. - Specify an id value to get the corresponding whoisRecord. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WhoisRecord]
        Find more info here: https://learn.microsoft.com/graph/api/security-whoisrecord-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.security.whois_record import WhoisRecord

        return await self.request_adapter.send_async(request_info, WhoisRecord, error_mapping)
    
    async def patch(self,body: Optional[WhoisRecord] = None, request_configuration: Optional[WhoisRecordItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[WhoisRecord]:
        """
        Update the navigation property whoisRecords in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WhoisRecord]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.security.whois_record import WhoisRecord

        return await self.request_adapter.send_async(request_info, WhoisRecord, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WhoisRecordItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property whoisRecords for security
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
    
    def to_get_request_information(self,request_configuration: Optional[WhoisRecordItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the specified whoisRecord resource.  Specify the desired whoisRecord in one of the following two ways:- Identify a host and get its current whoisRecord. - Specify an id value to get the corresponding whoisRecord. This API is available in the following national cloud deployments.
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
    
    def to_patch_request_information(self,body: Optional[WhoisRecord] = None, request_configuration: Optional[WhoisRecordItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property whoisRecords in security
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
    
    def with_url(self,raw_url: Optional[str] = None) -> WhoisRecordItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WhoisRecordItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WhoisRecordItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def history(self) -> HistoryRequestBuilder:
        """
        Provides operations to manage the history property of the microsoft.graph.security.whoisRecord entity.
        """
        from .history.history_request_builder import HistoryRequestBuilder

        return HistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host(self) -> HostRequestBuilder:
        """
        Provides operations to manage the host property of the microsoft.graph.security.whoisBaseRecord entity.
        """
        from .host.host_request_builder import HostRequestBuilder

        return HostRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WhoisRecordItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class WhoisRecordItemRequestBuilderGetQueryParameters():
        """
        Get the specified whoisRecord resource.  Specify the desired whoisRecord in one of the following two ways:- Identify a host and get its current whoisRecord. - Specify an id value to get the corresponding whoisRecord. This API is available in the following national cloud deployments.
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
    class WhoisRecordItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WhoisRecordItemRequestBuilder.WhoisRecordItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WhoisRecordItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    


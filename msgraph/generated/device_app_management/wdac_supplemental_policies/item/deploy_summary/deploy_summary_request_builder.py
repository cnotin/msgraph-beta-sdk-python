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
    from .....models.windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

class DeploySummaryRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deploySummary property of the microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeploySummaryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/wdacSupplementalPolicies/{windowsDefenderApplicationControlSupplementalPolicy%2Did}/deploySummary{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DeploySummaryRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property deploySummary for deviceAppManagement
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
    
    async def get(self,request_configuration: Optional[DeploySummaryRequestBuilderGetRequestConfiguration] = None) -> Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary]:
        """
        WindowsDefenderApplicationControl supplemental policy deployment summary.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary]
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
        from .....models.windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

        return await self.request_adapter.send_async(request_info, WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary, error_mapping)
    
    async def patch(self,body: Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = None, request_configuration: Optional[DeploySummaryRequestBuilderPatchRequestConfiguration] = None) -> Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary]:
        """
        Update the navigation property deploySummary in deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary]
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
        from .....models.windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

        return await self.request_adapter.send_async(request_info, WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeploySummaryRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property deploySummary for deviceAppManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeploySummaryRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        WindowsDefenderApplicationControl supplemental policy deployment summary.
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
    
    def to_patch_request_information(self,body: Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = None, request_configuration: Optional[DeploySummaryRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property deploySummary in deviceAppManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DeploySummaryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeploySummaryRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DeploySummaryRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeploySummaryRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DeploySummaryRequestBuilderGetQueryParameters():
        """
        WindowsDefenderApplicationControl supplemental policy deployment summary.
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
    class DeploySummaryRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DeploySummaryRequestBuilder.DeploySummaryRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeploySummaryRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    


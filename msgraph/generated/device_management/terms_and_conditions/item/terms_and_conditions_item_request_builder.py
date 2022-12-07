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

acceptance_statuses_request_builder = lazy_import('msgraph.generated.device_management.terms_and_conditions.item.acceptance_statuses.acceptance_statuses_request_builder')
terms_and_conditions_acceptance_status_item_request_builder = lazy_import('msgraph.generated.device_management.terms_and_conditions.item.acceptance_statuses.item.terms_and_conditions_acceptance_status_item_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_management.terms_and_conditions.item.assignments.assignments_request_builder')
terms_and_conditions_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.terms_and_conditions.item.assignments.item.terms_and_conditions_assignment_item_request_builder')
group_assignments_request_builder = lazy_import('msgraph.generated.device_management.terms_and_conditions.item.group_assignments.group_assignments_request_builder')
terms_and_conditions_group_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.terms_and_conditions.item.group_assignments.item.terms_and_conditions_group_assignment_item_request_builder')
terms_and_conditions = lazy_import('msgraph.generated.models.terms_and_conditions')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class TermsAndConditionsItemRequestBuilder():
    """
    Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
    """
    def acceptance_statuses(self) -> acceptance_statuses_request_builder.AcceptanceStatusesRequestBuilder:
        """
        Provides operations to manage the acceptanceStatuses property of the microsoft.graph.termsAndConditions entity.
        """
        return acceptance_statuses_request_builder.AcceptanceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.termsAndConditions entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def group_assignments(self) -> group_assignments_request_builder.GroupAssignmentsRequestBuilder:
        """
        Provides operations to manage the groupAssignments property of the microsoft.graph.termsAndConditions entity.
        """
        return group_assignments_request_builder.GroupAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def acceptance_statuses_by_id(self,id: str) -> terms_and_conditions_acceptance_status_item_request_builder.TermsAndConditionsAcceptanceStatusItemRequestBuilder:
        """
        Provides operations to manage the acceptanceStatuses property of the microsoft.graph.termsAndConditions entity.
        Args:
            id: Unique identifier of the item
        Returns: terms_and_conditions_acceptance_status_item_request_builder.TermsAndConditionsAcceptanceStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["termsAndConditionsAcceptanceStatus%2Did"] = id
        return terms_and_conditions_acceptance_status_item_request_builder.TermsAndConditionsAcceptanceStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignments_by_id(self,id: str) -> terms_and_conditions_assignment_item_request_builder.TermsAndConditionsAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.termsAndConditions entity.
        Args:
            id: Unique identifier of the item
        Returns: terms_and_conditions_assignment_item_request_builder.TermsAndConditionsAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["termsAndConditionsAssignment%2Did"] = id
        return terms_and_conditions_assignment_item_request_builder.TermsAndConditionsAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TermsAndConditionsItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/termsAndConditions/{termsAndConditions%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[TermsAndConditionsItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property termsAndConditions for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[TermsAndConditionsItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The terms and conditions associated with device management of the company.
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
    
    def create_patch_request_information(self,body: Optional[terms_and_conditions.TermsAndConditions] = None, request_configuration: Optional[TermsAndConditionsItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property termsAndConditions in deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[TermsAndConditionsItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property termsAndConditions for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[TermsAndConditionsItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[terms_and_conditions.TermsAndConditions]:
        """
        The terms and conditions associated with device management of the company.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[terms_and_conditions.TermsAndConditions]
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
        return await self.request_adapter.send_async(request_info, terms_and_conditions.TermsAndConditions, response_handler, error_mapping)
    
    def group_assignments_by_id(self,id: str) -> terms_and_conditions_group_assignment_item_request_builder.TermsAndConditionsGroupAssignmentItemRequestBuilder:
        """
        Provides operations to manage the groupAssignments property of the microsoft.graph.termsAndConditions entity.
        Args:
            id: Unique identifier of the item
        Returns: terms_and_conditions_group_assignment_item_request_builder.TermsAndConditionsGroupAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["termsAndConditionsGroupAssignment%2Did"] = id
        return terms_and_conditions_group_assignment_item_request_builder.TermsAndConditionsGroupAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[terms_and_conditions.TermsAndConditions] = None, request_configuration: Optional[TermsAndConditionsItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[terms_and_conditions.TermsAndConditions]:
        """
        Update the navigation property termsAndConditions in deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[terms_and_conditions.TermsAndConditions]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, terms_and_conditions.TermsAndConditions, response_handler, error_mapping)
    
    @dataclass
    class TermsAndConditionsItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TermsAndConditionsItemRequestBuilderGetQueryParameters():
        """
        The terms and conditions associated with device management of the company.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class TermsAndConditionsItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TermsAndConditionsItemRequestBuilder.TermsAndConditionsItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TermsAndConditionsItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    


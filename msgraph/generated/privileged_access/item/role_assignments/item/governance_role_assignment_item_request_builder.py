from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from .....models import governance_role_assignment
from .....models.o_data_errors import o_data_error
from .linked_eligible_role_assignment import linked_eligible_role_assignment_request_builder
from .resource import resource_request_builder
from .role_definition import role_definition_request_builder
from .subject import subject_request_builder

class GovernanceRoleAssignmentItemRequestBuilder():
    """
    Provides operations to manage the roleAssignments property of the microsoft.graph.privilegedAccess entity.
    """
    def linked_eligible_role_assignment(self) -> linked_eligible_role_assignment_request_builder.LinkedEligibleRoleAssignmentRequestBuilder:
        """
        Provides operations to manage the linkedEligibleRoleAssignment property of the microsoft.graph.governanceRoleAssignment entity.
        """
        return linked_eligible_role_assignment_request_builder.LinkedEligibleRoleAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    def resource(self) -> resource_request_builder.ResourceRequestBuilder:
        """
        Provides operations to manage the resource property of the microsoft.graph.governanceRoleAssignment entity.
        """
        return resource_request_builder.ResourceRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_definition(self) -> role_definition_request_builder.RoleDefinitionRequestBuilder:
        """
        Provides operations to manage the roleDefinition property of the microsoft.graph.governanceRoleAssignment entity.
        """
        return role_definition_request_builder.RoleDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def subject(self) -> subject_request_builder.SubjectRequestBuilder:
        """
        Provides operations to manage the subject property of the microsoft.graph.governanceRoleAssignment entity.
        """
        return subject_request_builder.SubjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GovernanceRoleAssignmentItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/privilegedAccess/{privilegedAccess%2Did}/roleAssignments/{governanceRoleAssignment%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[GovernanceRoleAssignmentItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleAssignments for privilegedAccess
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
    
    def create_get_request_information(self,request_configuration: Optional[GovernanceRoleAssignmentItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A collection of role assignments for the provider.
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
    
    def create_patch_request_information(self,body: Optional[governance_role_assignment.GovernanceRoleAssignment] = None, request_configuration: Optional[GovernanceRoleAssignmentItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleAssignments in privilegedAccess
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
    
    async def delete(self,request_configuration: Optional[GovernanceRoleAssignmentItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property roleAssignments for privilegedAccess
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
    
    async def get(self,request_configuration: Optional[GovernanceRoleAssignmentItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[governance_role_assignment.GovernanceRoleAssignment]:
        """
        A collection of role assignments for the provider.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[governance_role_assignment.GovernanceRoleAssignment]
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
        return await self.request_adapter.send_async(request_info, governance_role_assignment.GovernanceRoleAssignment, response_handler, error_mapping)
    
    async def patch(self,body: Optional[governance_role_assignment.GovernanceRoleAssignment] = None, request_configuration: Optional[GovernanceRoleAssignmentItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[governance_role_assignment.GovernanceRoleAssignment]:
        """
        Update the navigation property roleAssignments in privilegedAccess
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[governance_role_assignment.GovernanceRoleAssignment]
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
        return await self.request_adapter.send_async(request_info, governance_role_assignment.GovernanceRoleAssignment, response_handler, error_mapping)
    
    @dataclass
    class GovernanceRoleAssignmentItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GovernanceRoleAssignmentItemRequestBuilderGetQueryParameters():
        """
        A collection of role assignments for the provider.
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
    class GovernanceRoleAssignmentItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GovernanceRoleAssignmentItemRequestBuilder.GovernanceRoleAssignmentItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GovernanceRoleAssignmentItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    


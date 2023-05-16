from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.o_data_errors import o_data_error
    from .........models.security import ediscovery_review_set_query
    from .microsoft_graph_security_apply_tags import microsoft_graph_security_apply_tags_request_builder
    from .microsoft_graph_security_export import microsoft_graph_security_export_request_builder
    from .microsoft_graph_security_run import microsoft_graph_security_run_request_builder

class EdiscoveryReviewSetQueryItemRequestBuilder():
    """
    Provides operations to manage the queries property of the microsoft.graph.security.ediscoveryReviewSet entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EdiscoveryReviewSetQueryItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/reviewSets/{ediscoveryReviewSet%2Did}/queries/{ediscoveryReviewSetQuery%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[EdiscoveryReviewSetQueryItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an ediscoveryReviewSetQuery object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EdiscoveryReviewSetQueryItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery]:
        """
        Read the properties and relationships of an ediscoveryReviewSetQuery object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.security import ediscovery_review_set_query

        return await self.request_adapter.send_async(request_info, ediscovery_review_set_query.EdiscoveryReviewSetQuery, error_mapping)
    
    async def patch(self,body: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery] = None, request_configuration: Optional[EdiscoveryReviewSetQueryItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery]:
        """
        Update the properties of an ediscoveryReviewSetQuery object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.security import ediscovery_review_set_query

        return await self.request_adapter.send_async(request_info, ediscovery_review_set_query.EdiscoveryReviewSetQuery, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EdiscoveryReviewSetQueryItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an ediscoveryReviewSetQuery object.
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
    
    def to_get_request_information(self,request_configuration: Optional[EdiscoveryReviewSetQueryItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of an ediscoveryReviewSetQuery object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery] = None, request_configuration: Optional[EdiscoveryReviewSetQueryItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an ediscoveryReviewSetQuery object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def microsoft_graph_security_apply_tags(self) -> microsoft_graph_security_apply_tags_request_builder.MicrosoftGraphSecurityApplyTagsRequestBuilder:
        """
        Provides operations to call the applyTags method.
        """
        from .microsoft_graph_security_apply_tags import microsoft_graph_security_apply_tags_request_builder

        return microsoft_graph_security_apply_tags_request_builder.MicrosoftGraphSecurityApplyTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_export(self) -> microsoft_graph_security_export_request_builder.MicrosoftGraphSecurityExportRequestBuilder:
        """
        Provides operations to call the export method.
        """
        from .microsoft_graph_security_export import microsoft_graph_security_export_request_builder

        return microsoft_graph_security_export_request_builder.MicrosoftGraphSecurityExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_run(self) -> microsoft_graph_security_run_request_builder.MicrosoftGraphSecurityRunRequestBuilder:
        """
        Provides operations to call the run method.
        """
        from .microsoft_graph_security_run import microsoft_graph_security_run_request_builder

        return microsoft_graph_security_run_request_builder.MicrosoftGraphSecurityRunRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EdiscoveryReviewSetQueryItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EdiscoveryReviewSetQueryItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an ediscoveryReviewSetQuery object.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class EdiscoveryReviewSetQueryItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EdiscoveryReviewSetQueryItemRequestBuilder.EdiscoveryReviewSetQueryItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EdiscoveryReviewSetQueryItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    


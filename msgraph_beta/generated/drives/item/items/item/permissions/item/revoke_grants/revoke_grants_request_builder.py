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
    from ........models.o_data_errors.o_data_error import ODataError
    from ........models.permission import Permission
    from .revoke_grants_post_request_body import RevokeGrantsPostRequestBody

class RevokeGrantsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the revokeGrants method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RevokeGrantsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/permissions/{permission%2Did}/revokeGrants", path_parameters)
    
    async def post(self,body: Optional[RevokeGrantsPostRequestBody] = None, request_configuration: Optional[RevokeGrantsRequestBuilderPostRequestConfiguration] = None) -> Optional[Permission]:
        """
        Revoke access to a listItem][] or [driveItem][] granted via a sharing link by removing the specified [recipient][] from the link. This API is available in the following [national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Permission]
        Find more info here: https://learn.microsoft.com/graph/api/permission-revokegrants?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.permission import Permission

        return await self.request_adapter.send_async(request_info, Permission, error_mapping)
    
    def to_post_request_information(self,body: Optional[RevokeGrantsPostRequestBody] = None, request_configuration: Optional[RevokeGrantsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Revoke access to a listItem][] or [driveItem][] granted via a sharing link by removing the specified [recipient][] from the link. This API is available in the following [national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> RevokeGrantsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RevokeGrantsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RevokeGrantsRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RevokeGrantsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    


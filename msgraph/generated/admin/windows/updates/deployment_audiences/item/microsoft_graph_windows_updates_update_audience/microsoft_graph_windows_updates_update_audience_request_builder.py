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
    from . import update_audience_post_request_body
    from .......models.o_data_errors import o_data_error

class MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder():
    """
    Provides operations to call the updateAudience method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/windows/updates/deploymentAudiences/{deploymentAudience%2Did}/microsoft.graph.windowsUpdates.updateAudience"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,body: Optional[update_audience_post_request_body.UpdateAudiencePostRequestBody] = None, request_configuration: Optional[MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilderPostRequestConfiguration] = None) -> None:
        """
        Update the members and exclusions collections of a deploymentAudience. Adding an azureADDevice to the members or exclusions collections of a deployment audience automatically creates an Azure AD device object, if it does not already exist. If the same updatableAsset gets included in the **exclusions** and **members** collections of a **deploymentAudience**, deployment will not apply to that asset. If all **updatableAsset** objects are the same type, you can also use the method updateAudienceById to update the **deploymentAudience**.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,body: Optional[update_audience_post_request_body.UpdateAudiencePostRequestBody] = None, request_configuration: Optional[MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Update the members and exclusions collections of a deploymentAudience. Adding an azureADDevice to the members or exclusions collections of a deployment audience automatically creates an Azure AD device object, if it does not already exist. If the same updatableAsset gets included in the **exclusions** and **members** collections of a **deploymentAudience**, deployment will not apply to that asset. If all **updatableAsset** objects are the same type, you can also use the method updateAudienceById to update the **deploymentAudience**.
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
        request_info.http_method = Method.POST
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    


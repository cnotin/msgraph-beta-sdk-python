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
    from ......models.business_scenario_plan_reference import BusinessScenarioPlanReference
    from ......models.o_data_errors.o_data_error import ODataError
    from .get_plan_post_request_body import GetPlanPostRequestBody

class GetPlanRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getPlan method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GetPlanRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/businessScenarios/{businessScenario%2Did}/planner/getPlan", path_parameters)
    
    async def post(self,body: Optional[GetPlanPostRequestBody] = None, request_configuration: Optional[GetPlanRequestBuilderPostRequestConfiguration] = None) -> Optional[BusinessScenarioPlanReference]:
        """
        Get information about the plannerPlan mapped to a given target. If a plannerPlan doesn't exist for the specified target at the time of the request, a new plan will be created for the businessScenario. This API is available in the following national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BusinessScenarioPlanReference]
        Find more info here: https://learn.microsoft.com/graph/api/businessscenarioplanner-getplan?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.business_scenario_plan_reference import BusinessScenarioPlanReference

        return await self.request_adapter.send_async(request_info, BusinessScenarioPlanReference, error_mapping)
    
    def to_post_request_information(self,body: Optional[GetPlanPostRequestBody] = None, request_configuration: Optional[GetPlanRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Get information about the plannerPlan mapped to a given target. If a plannerPlan doesn't exist for the specified target at the time of the request, a new plan will be created for the businessScenario. This API is available in the following national cloud deployments.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> GetPlanRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetPlanRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GetPlanRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GetPlanRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    


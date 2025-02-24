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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.policy_root import PolicyRoot
    from .access_review_policy.access_review_policy_request_builder import AccessReviewPolicyRequestBuilder
    from .activity_based_timeout_policies.activity_based_timeout_policies_request_builder import ActivityBasedTimeoutPoliciesRequestBuilder
    from .admin_consent_request_policy.admin_consent_request_policy_request_builder import AdminConsentRequestPolicyRequestBuilder
    from .app_management_policies.app_management_policies_request_builder import AppManagementPoliciesRequestBuilder
    from .authentication_flows_policy.authentication_flows_policy_request_builder import AuthenticationFlowsPolicyRequestBuilder
    from .authentication_methods_policy.authentication_methods_policy_request_builder import AuthenticationMethodsPolicyRequestBuilder
    from .authentication_strength_policies.authentication_strength_policies_request_builder import AuthenticationStrengthPoliciesRequestBuilder
    from .authorization_policy.authorization_policy_request_builder import AuthorizationPolicyRequestBuilder
    from .b2c_authentication_methods_policy.b2c_authentication_methods_policy_request_builder import B2cAuthenticationMethodsPolicyRequestBuilder
    from .claims_mapping_policies.claims_mapping_policies_request_builder import ClaimsMappingPoliciesRequestBuilder
    from .conditional_access_policies.conditional_access_policies_request_builder import ConditionalAccessPoliciesRequestBuilder
    from .cross_tenant_access_policy.cross_tenant_access_policy_request_builder import CrossTenantAccessPolicyRequestBuilder
    from .default_app_management_policy.default_app_management_policy_request_builder import DefaultAppManagementPolicyRequestBuilder
    from .device_registration_policy.device_registration_policy_request_builder import DeviceRegistrationPolicyRequestBuilder
    from .directory_role_access_review_policy.directory_role_access_review_policy_request_builder import DirectoryRoleAccessReviewPolicyRequestBuilder
    from .external_identities_policy.external_identities_policy_request_builder import ExternalIdentitiesPolicyRequestBuilder
    from .feature_rollout_policies.feature_rollout_policies_request_builder import FeatureRolloutPoliciesRequestBuilder
    from .federated_token_validation_policy.federated_token_validation_policy_request_builder import FederatedTokenValidationPolicyRequestBuilder
    from .home_realm_discovery_policies.home_realm_discovery_policies_request_builder import HomeRealmDiscoveryPoliciesRequestBuilder
    from .identity_security_defaults_enforcement_policy.identity_security_defaults_enforcement_policy_request_builder import IdentitySecurityDefaultsEnforcementPolicyRequestBuilder
    from .mobile_app_management_policies.mobile_app_management_policies_request_builder import MobileAppManagementPoliciesRequestBuilder
    from .mobile_device_management_policies.mobile_device_management_policies_request_builder import MobileDeviceManagementPoliciesRequestBuilder
    from .permission_grant_policies.permission_grant_policies_request_builder import PermissionGrantPoliciesRequestBuilder
    from .role_management_policies.role_management_policies_request_builder import RoleManagementPoliciesRequestBuilder
    from .role_management_policy_assignments.role_management_policy_assignments_request_builder import RoleManagementPolicyAssignmentsRequestBuilder
    from .service_principal_creation_policies.service_principal_creation_policies_request_builder import ServicePrincipalCreationPoliciesRequestBuilder
    from .token_issuance_policies.token_issuance_policies_request_builder import TokenIssuancePoliciesRequestBuilder
    from .token_lifetime_policies.token_lifetime_policies_request_builder import TokenLifetimePoliciesRequestBuilder

class PoliciesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the policyRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PoliciesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/policies{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[PoliciesRequestBuilderGetRequestConfiguration] = None) -> Optional[PolicyRoot]:
        """
        Get policies
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PolicyRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.policy_root import PolicyRoot

        return await self.request_adapter.send_async(request_info, PolicyRoot, error_mapping)
    
    async def patch(self,body: Optional[PolicyRoot] = None, request_configuration: Optional[PoliciesRequestBuilderPatchRequestConfiguration] = None) -> Optional[PolicyRoot]:
        """
        Update policies
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PolicyRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.policy_root import PolicyRoot

        return await self.request_adapter.send_async(request_info, PolicyRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[PoliciesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get policies
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[PolicyRoot] = None, request_configuration: Optional[PoliciesRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update policies
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
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PoliciesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PoliciesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PoliciesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def access_review_policy(self) -> AccessReviewPolicyRequestBuilder:
        """
        Provides operations to manage the accessReviewPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .access_review_policy.access_review_policy_request_builder import AccessReviewPolicyRequestBuilder

        return AccessReviewPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def activity_based_timeout_policies(self) -> ActivityBasedTimeoutPoliciesRequestBuilder:
        """
        Provides operations to manage the activityBasedTimeoutPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .activity_based_timeout_policies.activity_based_timeout_policies_request_builder import ActivityBasedTimeoutPoliciesRequestBuilder

        return ActivityBasedTimeoutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def admin_consent_request_policy(self) -> AdminConsentRequestPolicyRequestBuilder:
        """
        Provides operations to manage the adminConsentRequestPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .admin_consent_request_policy.admin_consent_request_policy_request_builder import AdminConsentRequestPolicyRequestBuilder

        return AdminConsentRequestPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_management_policies(self) -> AppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .app_management_policies.app_management_policies_request_builder import AppManagementPoliciesRequestBuilder

        return AppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_flows_policy(self) -> AuthenticationFlowsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationFlowsPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .authentication_flows_policy.authentication_flows_policy_request_builder import AuthenticationFlowsPolicyRequestBuilder

        return AuthenticationFlowsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods_policy(self) -> AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .authentication_methods_policy.authentication_methods_policy_request_builder import AuthenticationMethodsPolicyRequestBuilder

        return AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_strength_policies(self) -> AuthenticationStrengthPoliciesRequestBuilder:
        """
        Provides operations to manage the authenticationStrengthPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .authentication_strength_policies.authentication_strength_policies_request_builder import AuthenticationStrengthPoliciesRequestBuilder

        return AuthenticationStrengthPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authorization_policy(self) -> AuthorizationPolicyRequestBuilder:
        """
        Provides operations to manage the authorizationPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .authorization_policy.authorization_policy_request_builder import AuthorizationPolicyRequestBuilder

        return AuthorizationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2c_authentication_methods_policy(self) -> B2cAuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the b2cAuthenticationMethodsPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .b2c_authentication_methods_policy.b2c_authentication_methods_policy_request_builder import B2cAuthenticationMethodsPolicyRequestBuilder

        return B2cAuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def claims_mapping_policies(self) -> ClaimsMappingPoliciesRequestBuilder:
        """
        Provides operations to manage the claimsMappingPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .claims_mapping_policies.claims_mapping_policies_request_builder import ClaimsMappingPoliciesRequestBuilder

        return ClaimsMappingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_policies(self) -> ConditionalAccessPoliciesRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .conditional_access_policies.conditional_access_policies_request_builder import ConditionalAccessPoliciesRequestBuilder

        return ConditionalAccessPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cross_tenant_access_policy(self) -> CrossTenantAccessPolicyRequestBuilder:
        """
        Provides operations to manage the crossTenantAccessPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .cross_tenant_access_policy.cross_tenant_access_policy_request_builder import CrossTenantAccessPolicyRequestBuilder

        return CrossTenantAccessPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_app_management_policy(self) -> DefaultAppManagementPolicyRequestBuilder:
        """
        Provides operations to manage the defaultAppManagementPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .default_app_management_policy.default_app_management_policy_request_builder import DefaultAppManagementPolicyRequestBuilder

        return DefaultAppManagementPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_registration_policy(self) -> DeviceRegistrationPolicyRequestBuilder:
        """
        Provides operations to manage the deviceRegistrationPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .device_registration_policy.device_registration_policy_request_builder import DeviceRegistrationPolicyRequestBuilder

        return DeviceRegistrationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_role_access_review_policy(self) -> DirectoryRoleAccessReviewPolicyRequestBuilder:
        """
        Provides operations to manage the directoryRoleAccessReviewPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .directory_role_access_review_policy.directory_role_access_review_policy_request_builder import DirectoryRoleAccessReviewPolicyRequestBuilder

        return DirectoryRoleAccessReviewPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_identities_policy(self) -> ExternalIdentitiesPolicyRequestBuilder:
        """
        Provides operations to manage the externalIdentitiesPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .external_identities_policy.external_identities_policy_request_builder import ExternalIdentitiesPolicyRequestBuilder

        return ExternalIdentitiesPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feature_rollout_policies(self) -> FeatureRolloutPoliciesRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .feature_rollout_policies.feature_rollout_policies_request_builder import FeatureRolloutPoliciesRequestBuilder

        return FeatureRolloutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federated_token_validation_policy(self) -> FederatedTokenValidationPolicyRequestBuilder:
        """
        Provides operations to manage the federatedTokenValidationPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .federated_token_validation_policy.federated_token_validation_policy_request_builder import FederatedTokenValidationPolicyRequestBuilder

        return FederatedTokenValidationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def home_realm_discovery_policies(self) -> HomeRealmDiscoveryPoliciesRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .home_realm_discovery_policies.home_realm_discovery_policies_request_builder import HomeRealmDiscoveryPoliciesRequestBuilder

        return HomeRealmDiscoveryPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_security_defaults_enforcement_policy(self) -> IdentitySecurityDefaultsEnforcementPolicyRequestBuilder:
        """
        Provides operations to manage the identitySecurityDefaultsEnforcementPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .identity_security_defaults_enforcement_policy.identity_security_defaults_enforcement_policy_request_builder import IdentitySecurityDefaultsEnforcementPolicyRequestBuilder

        return IdentitySecurityDefaultsEnforcementPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_management_policies(self) -> MobileAppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the mobileAppManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .mobile_app_management_policies.mobile_app_management_policies_request_builder import MobileAppManagementPoliciesRequestBuilder

        return MobileAppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_device_management_policies(self) -> MobileDeviceManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the mobileDeviceManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .mobile_device_management_policies.mobile_device_management_policies_request_builder import MobileDeviceManagementPoliciesRequestBuilder

        return MobileDeviceManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grant_policies(self) -> PermissionGrantPoliciesRequestBuilder:
        """
        Provides operations to manage the permissionGrantPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .permission_grant_policies.permission_grant_policies_request_builder import PermissionGrantPoliciesRequestBuilder

        return PermissionGrantPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management_policies(self) -> RoleManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .role_management_policies.role_management_policies_request_builder import RoleManagementPoliciesRequestBuilder

        return RoleManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management_policy_assignments(self) -> RoleManagementPolicyAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicyAssignments property of the microsoft.graph.policyRoot entity.
        """
        from .role_management_policy_assignments.role_management_policy_assignments_request_builder import RoleManagementPolicyAssignmentsRequestBuilder

        return RoleManagementPolicyAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal_creation_policies(self) -> ServicePrincipalCreationPoliciesRequestBuilder:
        """
        Provides operations to manage the servicePrincipalCreationPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .service_principal_creation_policies.service_principal_creation_policies_request_builder import ServicePrincipalCreationPoliciesRequestBuilder

        return ServicePrincipalCreationPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_issuance_policies(self) -> TokenIssuancePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.policyRoot entity.
        """
        from .token_issuance_policies.token_issuance_policies_request_builder import TokenIssuancePoliciesRequestBuilder

        return TokenIssuancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_lifetime_policies(self) -> TokenLifetimePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.policyRoot entity.
        """
        from .token_lifetime_policies.token_lifetime_policies_request_builder import TokenLifetimePoliciesRequestBuilder

        return TokenLifetimePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PoliciesRequestBuilderGetQueryParameters():
        """
        Get policies
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
    class PoliciesRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PoliciesRequestBuilder.PoliciesRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PoliciesRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    


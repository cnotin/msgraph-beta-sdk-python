from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
    from .cloud_pc_management_service import CloudPcManagementService
    from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
    from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
    from .cloud_pc_provisioning_type import CloudPcProvisioningType
    from .cloud_pc_windows_settings import CloudPcWindowsSettings
    from .entity import Entity
    from .microsoft_managed_desktop import MicrosoftManagedDesktop

from .entity import Entity

@dataclass
class CloudPcProvisioningPolicy(Entity):
    # The URL of the alternate resource that links to this provisioning policy. Read-only.
    alternate_resource_url: Optional[str] = None
    # A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. For an example about how to get the assignments relationship, see Get cloudPcProvisioningPolicy.
    assignments: Optional[List[CloudPcProvisioningPolicyAssignment]] = None
    # The display name of the Cloud PC group that the Cloud PCs reside in. Read-only.
    cloud_pc_group_display_name: Optional[str] = None
    # The template used to name Cloud PCs provisioned using this policy. This can contain custom text and replacement tokens, including %USERNAME:x% and %RAND:x%, which represent the user's name and a randomly generated number, respectively. For example, 'CPC-%USERNAME:4%-%RAND:5%' means that the Cloud PC's name will start with 'CPC-', have a four-character username in the middle followed by a '-' character, and end with five random characters. The total length of the text generated by the template can be no more than 15 characters. Supports $filter, $select, $orderBy.
    cloud_pc_naming_template: Optional[str] = None
    # The provisioning policy description.
    description: Optional[str] = None
    # The display name for the provisioning policy.
    display_name: Optional[str] = None
    # Specifies how Cloud PCs will join Azure Active Directory.
    domain_join_configuration: Optional[CloudPcDomainJoinConfiguration] = None
    # The domainJoinConfigurations property
    domain_join_configurations: Optional[List[CloudPcDomainJoinConfiguration]] = None
    # True if the provisioned Cloud PC can be accessed by single sign-on. False indicates that the provisioned Cloud PC doesn't support this feature. Default value is false. Windows 365 users can use single sign-on to authenticate to Azure Active Directory (Azure AD) with passwordless options (for example, FIDO keys) to access their Cloud PC. Optional.
    enable_single_sign_on: Optional[bool] = None
    # The number of hours to wait before reprovisioning/deprovisioning happens. Read-only.
    grace_period_in_hours: Optional[int] = None
    # The display name for the OS image you’re provisioning.
    image_display_name: Optional[str] = None
    # The ID of the OS image you want to provision on Cloud PCs. The format for a gallery type image is: {publisheroffersku}. Supported values for each of the parameters are as follows:publisher: Microsoftwindowsdesktop. offer: windows-ent-cpc. sku: 21h1-ent-cpc-m365, 21h1-ent-cpc-os, 20h2-ent-cpc-m365, 20h2-ent-cpc-os, 20h1-ent-cpc-m365, 20h1-ent-cpc-os, 19h2-ent-cpc-m365 and 19h2-ent-cpc-os.
    image_id: Optional[str] = None
    # The imageType property
    image_type: Optional[CloudPcProvisioningPolicyImageType] = None
    # Indicates whether the local admin option is enabled. If the local admin option is enabled, the end user can be an admin of the Cloud PC device. Read-only.
    local_admin_enabled: Optional[bool] = None
    # The managedBy property
    managed_by: Optional[CloudPcManagementService] = None
    # The specific settings for the Microsoft Managed Desktop, which enables customers to get a managed device experience for the Cloud PC. Before you can enable Microsoft Managed Desktop, an admin must configure it.
    microsoft_managed_desktop: Optional[MicrosoftManagedDesktop] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the cloudPcOnPremisesConnection. To ensure that Cloud PCs have network connectivity and that they domain join, choose a connection with a virtual network that’s validated by the Cloud PC service.
    on_premises_connection_id: Optional[str] = None
    # Specifies the type of license used when provisioning Cloud PCs using this policy. By default, the license type is dedicated if the provisioningType isn't specified when you create the cloudPcProvisioningPolicy. You can't change this property after the cloudPcProvisioningPolicy was created. Possible values are: dedicated, shared, unknownFutureValue.
    provisioning_type: Optional[CloudPcProvisioningType] = None
    # Specific Windows settings to configure while creating Cloud PCs for this provisioning policy.
    windows_settings: Optional[CloudPcWindowsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcProvisioningPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcProvisioningPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcProvisioningPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .cloud_pc_windows_settings import CloudPcWindowsSettings
        from .entity import Entity
        from .microsoft_managed_desktop import MicrosoftManagedDesktop

        from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .cloud_pc_windows_settings import CloudPcWindowsSettings
        from .entity import Entity
        from .microsoft_managed_desktop import MicrosoftManagedDesktop

        fields: Dict[str, Callable[[Any], None]] = {
            "alternateResourceUrl": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(CloudPcProvisioningPolicyAssignment)),
            "cloudPcGroupDisplayName": lambda n : setattr(self, 'cloud_pc_group_display_name', n.get_str_value()),
            "cloudPcNamingTemplate": lambda n : setattr(self, 'cloud_pc_naming_template', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainJoinConfiguration": lambda n : setattr(self, 'domain_join_configuration', n.get_object_value(CloudPcDomainJoinConfiguration)),
            "domainJoinConfigurations": lambda n : setattr(self, 'domain_join_configurations', n.get_collection_of_object_values(CloudPcDomainJoinConfiguration)),
            "enableSingleSignOn": lambda n : setattr(self, 'enable_single_sign_on', n.get_bool_value()),
            "gracePeriodInHours": lambda n : setattr(self, 'grace_period_in_hours', n.get_int_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "imageId": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "imageType": lambda n : setattr(self, 'image_type', n.get_enum_value(CloudPcProvisioningPolicyImageType)),
            "localAdminEnabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_enum_value(CloudPcManagementService)),
            "microsoftManagedDesktop": lambda n : setattr(self, 'microsoft_managed_desktop', n.get_object_value(MicrosoftManagedDesktop)),
            "onPremisesConnectionId": lambda n : setattr(self, 'on_premises_connection_id', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(CloudPcProvisioningType)),
            "windowsSettings": lambda n : setattr(self, 'windows_settings', n.get_object_value(CloudPcWindowsSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("alternateResourceUrl", self.alternate_resource_url)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("cloudPcGroupDisplayName", self.cloud_pc_group_display_name)
        writer.write_str_value("cloudPcNamingTemplate", self.cloud_pc_naming_template)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("domainJoinConfiguration", self.domain_join_configuration)
        writer.write_collection_of_object_values("domainJoinConfigurations", self.domain_join_configurations)
        writer.write_bool_value("enableSingleSignOn", self.enable_single_sign_on)
        writer.write_int_value("gracePeriodInHours", self.grace_period_in_hours)
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_str_value("imageId", self.image_id)
        writer.write_enum_value("imageType", self.image_type)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_enum_value("managedBy", self.managed_by)
        writer.write_object_value("microsoftManagedDesktop", self.microsoft_managed_desktop)
        writer.write_str_value("onPremisesConnectionId", self.on_premises_connection_id)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_object_value("windowsSettings", self.windows_settings)
    


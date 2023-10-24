from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .azure_group import AzureGroup
    from .azure_managed_identity import AzureManagedIdentity
    from .azure_serverless_function import AzureServerlessFunction
    from .azure_service_principal import AzureServicePrincipal
    from .azure_user import AzureUser

from .authorization_system_identity import AuthorizationSystemIdentity

@dataclass
class AzureIdentity(AuthorizationSystemIdentity):
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.azureIdentity"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureGroup".casefold():
            from .azure_group import AzureGroup

            return AzureGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureManagedIdentity".casefold():
            from .azure_managed_identity import AzureManagedIdentity

            return AzureManagedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureServerlessFunction".casefold():
            from .azure_serverless_function import AzureServerlessFunction

            return AzureServerlessFunction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureServicePrincipal".casefold():
            from .azure_service_principal import AzureServicePrincipal

            return AzureServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureUser".casefold():
            from .azure_user import AzureUser

            return AzureUser()
        return AzureIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .azure_group import AzureGroup
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_serverless_function import AzureServerlessFunction
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser

        from .authorization_system_identity import AuthorizationSystemIdentity
        from .azure_group import AzureGroup
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_serverless_function import AzureServerlessFunction
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser

        fields: Dict[str, Callable[[Any], None]] = {
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
    


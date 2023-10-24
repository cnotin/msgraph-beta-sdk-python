from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

@dataclass
class AzureAdTokenAuthentication(CustomExtensionAuthenticationConfiguration):
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.azureAdTokenAuthentication"
    # The appID of the Microsoft Entra application to use to authenticate a logic app with a custom access package workflow extension.
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureAdTokenAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureAdTokenAuthentication
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AzureAdTokenAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

        from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
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
        writer.write_str_value("resourceId", self.resource_id)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disable_user_entity_identifier import DisableUserEntityIdentifier
    from .response_action import ResponseAction

from .response_action import ResponseAction

@dataclass
class DisableUserResponseAction(ResponseAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.disableUserResponseAction"
    # The identifier property
    identifier: Optional[DisableUserEntityIdentifier] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DisableUserResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DisableUserResponseAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DisableUserResponseAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .disable_user_entity_identifier import DisableUserEntityIdentifier
        from .response_action import ResponseAction

        from .disable_user_entity_identifier import DisableUserEntityIdentifier
        from .response_action import ResponseAction

        fields: Dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_enum_value(DisableUserEntityIdentifier)),
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
        writer.write_enum_value("identifier", self.identifier)
    


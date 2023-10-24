from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .information_protection import InformationProtection

from ..entity import Entity

@dataclass
class Security(Entity):
    # The informationProtection property
    information_protection: Optional[InformationProtection] = None
    # The OdataType property
    OdataType: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Security:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Security
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Security()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .information_protection import InformationProtection

        from ..entity import Entity
        from .information_protection import InformationProtection

        fields: Dict[str, Callable[[Any], None]] = {
            "informationProtection": lambda n : setattr(self, 'information_protection', n.get_object_value(InformationProtection)),
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
        writer.write_object_value("informationProtection", self.information_protection)
    


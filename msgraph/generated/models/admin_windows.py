from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin_windows_updates import AdminWindowsUpdates
    from .entity import Entity

from .entity import Entity

@dataclass
class AdminWindows(Entity):
    # The OdataType property
    OdataType: Optional[str] = None
    # Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
    updates: Optional[AdminWindowsUpdates] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminWindows:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminWindows
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AdminWindows()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .admin_windows_updates import AdminWindowsUpdates
        from .entity import Entity

        from .admin_windows_updates import AdminWindowsUpdates
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "updates": lambda n : setattr(self, 'updates', n.get_object_value(AdminWindowsUpdates)),
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
        writer.write_object_value("updates", self.updates)
    


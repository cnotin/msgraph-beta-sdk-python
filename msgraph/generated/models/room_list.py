from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place
    from .room import Room
    from .workspace import Workspace

from .place import Place

@dataclass
class RoomList(Place):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.roomList"
    # The email address of the room list.
    email_address: Optional[str] = None
    # The rooms property
    rooms: Optional[List[Room]] = None
    # The workspaces property
    workspaces: Optional[List[Workspace]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoomList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoomList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RoomList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place
        from .room import Room
        from .workspace import Workspace

        from .place import Place
        from .room import Room
        from .workspace import Workspace

        fields: Dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "rooms": lambda n : setattr(self, 'rooms', n.get_collection_of_object_values(Room)),
            "workspaces": lambda n : setattr(self, 'workspaces', n.get_collection_of_object_values(Workspace)),
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
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_collection_of_object_values("rooms", self.rooms)
        writer.write_collection_of_object_values("workspaces", self.workspaces)
    


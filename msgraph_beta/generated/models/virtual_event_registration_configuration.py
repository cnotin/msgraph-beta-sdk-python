from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event_registration_question import VirtualEventRegistrationQuestion
    from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

from .entity import Entity

@dataclass
class VirtualEventRegistrationConfiguration(Entity):
    # Total capacity of the virtual event.
    capacity: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registration questions.
    questions: Optional[List[VirtualEventRegistrationQuestion]] = None
    # Registration URL of the virtual event.
    registration_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistrationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinarRegistrationConfiguration".casefold():
            from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

            return VirtualEventWebinarRegistrationConfiguration()
        return VirtualEventRegistrationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event_registration_question import VirtualEventRegistrationQuestion
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

        from .entity import Entity
        from .virtual_event_registration_question import VirtualEventRegistrationQuestion
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(VirtualEventRegistrationQuestion)),
            "registrationWebUrl": lambda n : setattr(self, 'registration_web_url', n.get_str_value()),
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
        writer.write_int_value("capacity", self.capacity)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_str_value("registrationWebUrl", self.registration_web_url)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SelfActivatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The duration property
    duration: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The ticketNumber property
    ticket_number: Optional[str] = None
    # The ticketSystem property
    ticket_system: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SelfActivatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelfActivatePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SelfActivatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "duration": lambda n : setattr(self, 'duration', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "ticketNumber": lambda n : setattr(self, 'ticket_number', n.get_str_value()),
            "ticketSystem": lambda n : setattr(self, 'ticket_system', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("duration", self.duration)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("ticketNumber", self.ticket_number)
        writer.write_str_value("ticketSystem", self.ticket_system)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .time_card_break import TimeCardBreak
    from .time_card_event import TimeCardEvent

@dataclass
class TimeCardEntry(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The list of breaks associated with the timeCard.
    breaks: Optional[List[TimeCardBreak]] = None
    # The clock-in event of the timeCard.
    clock_in_event: Optional[TimeCardEvent] = None
    # The clock-out event of the timeCard.
    clock_out_event: Optional[TimeCardEvent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeCardEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeCardEntry
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TimeCardEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .time_card_break import TimeCardBreak
        from .time_card_event import TimeCardEvent

        from .time_card_break import TimeCardBreak
        from .time_card_event import TimeCardEvent

        fields: Dict[str, Callable[[Any], None]] = {
            "breaks": lambda n : setattr(self, 'breaks', n.get_collection_of_object_values(TimeCardBreak)),
            "clockInEvent": lambda n : setattr(self, 'clock_in_event', n.get_object_value(TimeCardEvent)),
            "clockOutEvent": lambda n : setattr(self, 'clock_out_event', n.get_object_value(TimeCardEvent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("breaks", self.breaks)
        writer.write_object_value("clockInEvent", self.clock_in_event)
        writer.write_object_value("clockOutEvent", self.clock_out_event)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


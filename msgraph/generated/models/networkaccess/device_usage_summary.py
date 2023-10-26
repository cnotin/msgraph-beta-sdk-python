from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceUsageSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of distinct device IDs in the time frame between endDateTime and discoveryPivotDateTime.
    active_device_count: Optional[int] = None
    # The number of distinct device IDs havn't seen in the time frame between endDateTime and discoveryPivotDateTime but have seen in the time frame between discoveryPivotDateTime and startDateTime.
    inactive_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of distinct device IDs in the time frame between startDateTime and endDateTime.
    total_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceUsageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceUsageSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceUsageSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "activeDeviceCount": lambda n : setattr(self, 'active_device_count', n.get_int_value()),
            "inactiveDeviceCount": lambda n : setattr(self, 'inactive_device_count', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalDeviceCount": lambda n : setattr(self, 'total_device_count', n.get_int_value()),
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
        writer.write_int_value("activeDeviceCount", self.active_device_count)
        writer.write_int_value("inactiveDeviceCount", self.inactive_device_count)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("totalDeviceCount", self.total_device_count)
        writer.write_additional_data_value(self.additional_data)
    


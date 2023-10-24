from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

@dataclass
class DeviceHealthScriptHourlySchedule(DeviceHealthScriptRunSchedule):
    """
    Type of Device health script hourly schedule.
    """
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.deviceHealthScriptHourlySchedule"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptHourlySchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptHourlySchedule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptHourlySchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

        from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

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
    


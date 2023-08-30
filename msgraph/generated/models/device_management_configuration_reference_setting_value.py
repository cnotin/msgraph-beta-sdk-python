from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

@dataclass
class DeviceManagementConfigurationReferenceSettingValue(DeviceManagementConfigurationStringSettingValue):
    """
    Model for ReferenceSettingValue
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue"
    # A note that admin can use to put some contextual information
    note: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationReferenceSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationReferenceSettingValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationReferenceSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

        from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue

        fields: Dict[str, Callable[[Any], None]] = {
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
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
        writer.write_str_value("note", self.note)
    


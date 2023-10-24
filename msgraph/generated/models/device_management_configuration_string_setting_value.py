from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
    from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

@dataclass
class DeviceManagementConfigurationStringSettingValue(DeviceManagementConfigurationSimpleSettingValue):
    """
    Simple setting value
    """
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.deviceManagementConfigurationStringSettingValue"
    # Value of the string setting.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationStringSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue".casefold():
            from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue

            return DeviceManagementConfigurationReferenceSettingValue()
        return DeviceManagementConfigurationStringSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

        from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("value", self.value)
    


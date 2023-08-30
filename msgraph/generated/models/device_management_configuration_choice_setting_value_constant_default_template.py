from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate

@dataclass
class DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate(DeviceManagementConfigurationChoiceSettingValueDefaultTemplate):
    """
    Choice Setting Value Constant Default Template
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate"
    # Option Children
    children: Optional[List[DeviceManagementConfigurationSettingInstanceTemplate]] = None
    # Default Constant Value
    setting_definition_option_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(DeviceManagementConfigurationSettingInstanceTemplate)),
            "settingDefinitionOptionId": lambda n : setattr(self, 'setting_definition_option_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("settingDefinitionOptionId", self.setting_definition_option_id)
    


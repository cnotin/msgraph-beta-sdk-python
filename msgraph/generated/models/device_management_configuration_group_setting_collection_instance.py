from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
    from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

@dataclass
class DeviceManagementConfigurationGroupSettingCollectionInstance(DeviceManagementConfigurationSettingInstance):
    """
    Instance of a GroupSettingCollection
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance"
    # A collection of GroupSetting values
    group_setting_collection_value: Optional[List[DeviceManagementConfigurationGroupSettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationGroupSettingCollectionInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingCollectionInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationGroupSettingCollectionInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
        from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

        from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
        from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

        fields: Dict[str, Callable[[Any], None]] = {
            "groupSettingCollectionValue": lambda n : setattr(self, 'group_setting_collection_value', n.get_collection_of_object_values(DeviceManagementConfigurationGroupSettingValue)),
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
        writer.write_collection_of_object_values("groupSettingCollectionValue", self.group_setting_collection_value)
    


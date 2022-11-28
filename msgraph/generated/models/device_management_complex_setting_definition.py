from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import device_management_setting_definition

class DeviceManagementComplexSettingDefinition(device_management_setting_definition.DeviceManagementSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementComplexSettingDefinition and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The definitions of each property of the complex setting
        self._property_definition_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementComplexSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementComplexSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementComplexSettingDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "property_definition_ids": lambda n : setattr(self, 'property_definition_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def property_definition_ids(self,) -> Optional[List[str]]:
        """
        Gets the propertyDefinitionIds property value. The definitions of each property of the complex setting
        Returns: Optional[List[str]]
        """
        return self._property_definition_ids
    
    @property_definition_ids.setter
    def property_definition_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the propertyDefinitionIds property value. The definitions of each property of the complex setting
        Args:
            value: Value to set for the propertyDefinitionIds property.
        """
        self._property_definition_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("propertyDefinitionIds", self.property_definition_ids)
    


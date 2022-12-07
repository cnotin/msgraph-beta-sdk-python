from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_presentation_value = lazy_import('msgraph.generated.models.group_policy_presentation_value')

class GroupPolicyPresentationValueBoolean(group_policy_presentation_value.GroupPolicyPresentationValue):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationValueBoolean and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # An boolean value for the associated presentation.
        self._value: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationValueBoolean:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValueBoolean
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationValueBoolean()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "value": lambda n : setattr(self, 'value', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("value", self.value)
    
    @property
    def value(self,) -> Optional[bool]:
        """
        Gets the value property value. An boolean value for the associated presentation.
        Returns: Optional[bool]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[bool] = None) -> None:
        """
        Sets the value property value. An boolean value for the associated presentation.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    


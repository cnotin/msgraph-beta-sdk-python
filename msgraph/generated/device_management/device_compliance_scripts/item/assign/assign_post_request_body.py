from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_health_script_assignment = lazy_import('msgraph.generated.models.device_health_script_assignment')

class AssignPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assign method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceHealthScriptAssignments property
        self._device_health_script_assignments: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignPostRequestBody()
    
    @property
    def device_health_script_assignments(self,) -> Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]]:
        """
        Gets the deviceHealthScriptAssignments property value. The deviceHealthScriptAssignments property
        Returns: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]]
        """
        return self._device_health_script_assignments
    
    @device_health_script_assignments.setter
    def device_health_script_assignments(self,value: Optional[List[device_health_script_assignment.DeviceHealthScriptAssignment]] = None) -> None:
        """
        Sets the deviceHealthScriptAssignments property value. The deviceHealthScriptAssignments property
        Args:
            value: Value to set for the deviceHealthScriptAssignments property.
        """
        self._device_health_script_assignments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_health_script_assignments": lambda n : setattr(self, 'device_health_script_assignments', n.get_collection_of_object_values(device_health_script_assignment.DeviceHealthScriptAssignment)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("deviceHealthScriptAssignments", self.device_health_script_assignments)
        writer.write_additional_data_value(self.additional_data)
    


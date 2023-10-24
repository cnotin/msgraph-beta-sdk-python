from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.device_configuration_assignment import DeviceConfigurationAssignment
    from .....models.device_configuration_group_assignment import DeviceConfigurationGroupAssignment

@dataclass
class AssignPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The assignments property
    assignments: Optional[List[DeviceConfigurationAssignment]] = None
    # The deviceConfigurationGroupAssignments property
    device_configuration_group_assignments: Optional[List[DeviceConfigurationGroupAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.device_configuration_assignment import DeviceConfigurationAssignment
        from .....models.device_configuration_group_assignment import DeviceConfigurationGroupAssignment

        from .....models.device_configuration_assignment import DeviceConfigurationAssignment
        from .....models.device_configuration_group_assignment import DeviceConfigurationGroupAssignment

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceConfigurationAssignment)),
            "deviceConfigurationGroupAssignments": lambda n : setattr(self, 'device_configuration_group_assignments', n.get_collection_of_object_values(DeviceConfigurationGroupAssignment)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("deviceConfigurationGroupAssignments", self.device_configuration_group_assignments)
        writer.write_additional_data_value(self.additional_data)
    


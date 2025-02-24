from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_container_type import PlannerContainerType
    from .planner_shared_with_container import PlannerSharedWithContainer

@dataclass
class PlannerPlanContainer(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The identifier of the resource that contains the plan. Optional.
    container_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the resource that contains the plan. For supported types, see the previous table. Possible values are: group, unknownFutureValue, roster, project and driveItem. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: roster, project, driveItem. Optional.
    type: Optional[PlannerContainerType] = None
    # The full canonical URL of the container. Optional.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanContainer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerSharedWithContainer".casefold():
            from .planner_shared_with_container import PlannerSharedWithContainer

            return PlannerSharedWithContainer()
        return PlannerPlanContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .planner_container_type import PlannerContainerType
        from .planner_shared_with_container import PlannerSharedWithContainer

        from .planner_container_type import PlannerContainerType
        from .planner_shared_with_container import PlannerSharedWithContainer

        fields: Dict[str, Callable[[Any], None]] = {
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PlannerContainerType)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("containerId", self.container_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    


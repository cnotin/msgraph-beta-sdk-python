from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_plan_access_level import PlannerPlanAccessLevel
    from .planner_plan_container import PlannerPlanContainer

from .planner_plan_container import PlannerPlanContainer

@dataclass
class PlannerSharedWithContainer(PlannerPlanContainer):
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.plannerSharedWithContainer"
    # The accessLevel property
    access_level: Optional[PlannerPlanAccessLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerSharedWithContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerSharedWithContainer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerSharedWithContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .planner_plan_access_level import PlannerPlanAccessLevel
        from .planner_plan_container import PlannerPlanContainer

        from .planner_plan_access_level import PlannerPlanAccessLevel
        from .planner_plan_container import PlannerPlanContainer

        fields: Dict[str, Callable[[Any], None]] = {
            "accessLevel": lambda n : setattr(self, 'access_level', n.get_enum_value(PlannerPlanAccessLevel)),
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
        writer.write_enum_value("accessLevel", self.access_level)
    


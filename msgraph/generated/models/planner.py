from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_bucket import PlannerBucket
    from .planner_plan import PlannerPlan
    from .planner_roster import PlannerRoster
    from .planner_task import PlannerTask

from .entity import Entity

@dataclass
class Planner(Entity):
    # Read-only. Nullable. Returns a collection of the specified buckets
    buckets: Optional[List[PlannerBucket]] = None
    # The OdataType property
    OdataType: Optional[str] = None
    # Read-only. Nullable. Returns a collection of the specified plans
    plans: Optional[List[PlannerPlan]] = None
    # Read-only. Nullable. Returns a collection of the specified rosters
    rosters: Optional[List[PlannerRoster]] = None
    # Read-only. Nullable. Returns a collection of the specified tasks
    tasks: Optional[List[PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Planner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Planner
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Planner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_bucket import PlannerBucket
        from .planner_plan import PlannerPlan
        from .planner_roster import PlannerRoster
        from .planner_task import PlannerTask

        from .entity import Entity
        from .planner_bucket import PlannerBucket
        from .planner_plan import PlannerPlan
        from .planner_roster import PlannerRoster
        from .planner_task import PlannerTask

        fields: Dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(PlannerBucket)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(PlannerPlan)),
            "rosters": lambda n : setattr(self, 'rosters', n.get_collection_of_object_values(PlannerRoster)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
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
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_collection_of_object_values("rosters", self.rosters)
        writer.write_collection_of_object_values("tasks", self.tasks)
    


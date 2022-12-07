from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_external_task_source_display_type = lazy_import('msgraph.generated.models.planner_external_task_source_display_type')
planner_task_creation = lazy_import('msgraph.generated.models.planner_task_creation')

class PlannerExternalTaskSource(planner_task_creation.PlannerTaskCreation):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerExternalTaskSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerExternalTaskSource"
        # The contextScenarioId property
        self._context_scenario_id: Optional[str] = None
        # The displayLinkType property
        self._display_link_type: Optional[planner_external_task_source_display_type.PlannerExternalTaskSourceDisplayType] = None
        # The displayNameSegments property
        self._display_name_segments: Optional[List[str]] = None
        # The externalContextId property
        self._external_context_id: Optional[str] = None
        # The externalObjectId property
        self._external_object_id: Optional[str] = None
        # The externalObjectVersion property
        self._external_object_version: Optional[str] = None
        # The webUrl property
        self._web_url: Optional[str] = None
    
    @property
    def context_scenario_id(self,) -> Optional[str]:
        """
        Gets the contextScenarioId property value. The contextScenarioId property
        Returns: Optional[str]
        """
        return self._context_scenario_id
    
    @context_scenario_id.setter
    def context_scenario_id(self,value: Optional[str] = None) -> None:
        """
        Sets the contextScenarioId property value. The contextScenarioId property
        Args:
            value: Value to set for the contextScenarioId property.
        """
        self._context_scenario_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerExternalTaskSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerExternalTaskSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerExternalTaskSource()
    
    @property
    def display_link_type(self,) -> Optional[planner_external_task_source_display_type.PlannerExternalTaskSourceDisplayType]:
        """
        Gets the displayLinkType property value. The displayLinkType property
        Returns: Optional[planner_external_task_source_display_type.PlannerExternalTaskSourceDisplayType]
        """
        return self._display_link_type
    
    @display_link_type.setter
    def display_link_type(self,value: Optional[planner_external_task_source_display_type.PlannerExternalTaskSourceDisplayType] = None) -> None:
        """
        Sets the displayLinkType property value. The displayLinkType property
        Args:
            value: Value to set for the displayLinkType property.
        """
        self._display_link_type = value
    
    @property
    def display_name_segments(self,) -> Optional[List[str]]:
        """
        Gets the displayNameSegments property value. The displayNameSegments property
        Returns: Optional[List[str]]
        """
        return self._display_name_segments
    
    @display_name_segments.setter
    def display_name_segments(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the displayNameSegments property value. The displayNameSegments property
        Args:
            value: Value to set for the displayNameSegments property.
        """
        self._display_name_segments = value
    
    @property
    def external_context_id(self,) -> Optional[str]:
        """
        Gets the externalContextId property value. The externalContextId property
        Returns: Optional[str]
        """
        return self._external_context_id
    
    @external_context_id.setter
    def external_context_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalContextId property value. The externalContextId property
        Args:
            value: Value to set for the externalContextId property.
        """
        self._external_context_id = value
    
    @property
    def external_object_id(self,) -> Optional[str]:
        """
        Gets the externalObjectId property value. The externalObjectId property
        Returns: Optional[str]
        """
        return self._external_object_id
    
    @external_object_id.setter
    def external_object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectId property value. The externalObjectId property
        Args:
            value: Value to set for the externalObjectId property.
        """
        self._external_object_id = value
    
    @property
    def external_object_version(self,) -> Optional[str]:
        """
        Gets the externalObjectVersion property value. The externalObjectVersion property
        Returns: Optional[str]
        """
        return self._external_object_version
    
    @external_object_version.setter
    def external_object_version(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectVersion property value. The externalObjectVersion property
        Args:
            value: Value to set for the externalObjectVersion property.
        """
        self._external_object_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "context_scenario_id": lambda n : setattr(self, 'context_scenario_id', n.get_str_value()),
            "display_link_type": lambda n : setattr(self, 'display_link_type', n.get_enum_value(planner_external_task_source_display_type.PlannerExternalTaskSourceDisplayType)),
            "display_name_segments": lambda n : setattr(self, 'display_name_segments', n.get_collection_of_primitive_values(str)),
            "external_context_id": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "external_object_id": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
            "external_object_version": lambda n : setattr(self, 'external_object_version', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("contextScenarioId", self.context_scenario_id)
        writer.write_enum_value("displayLinkType", self.display_link_type)
        writer.write_collection_of_primitive_values("displayNameSegments", self.display_name_segments)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
        writer.write_str_value("externalObjectVersion", self.external_object_version)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The webUrl property
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The webUrl property
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    


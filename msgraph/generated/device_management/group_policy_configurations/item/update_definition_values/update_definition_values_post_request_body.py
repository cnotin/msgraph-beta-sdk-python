from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.group_policy_definition_value import GroupPolicyDefinitionValue

@dataclass
class UpdateDefinitionValuesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The added property
    added: Optional[List[GroupPolicyDefinitionValue]] = None
    # The deletedIds property
    deleted_ids: Optional[List[str]] = None
    # The updated property
    updated: Optional[List[GroupPolicyDefinitionValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateDefinitionValuesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateDefinitionValuesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateDefinitionValuesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.group_policy_definition_value import GroupPolicyDefinitionValue

        from .....models.group_policy_definition_value import GroupPolicyDefinitionValue

        fields: Dict[str, Callable[[Any], None]] = {
            "added": lambda n : setattr(self, 'added', n.get_collection_of_object_values(GroupPolicyDefinitionValue)),
            "deletedIds": lambda n : setattr(self, 'deleted_ids', n.get_collection_of_primitive_values(str)),
            "updated": lambda n : setattr(self, 'updated', n.get_collection_of_object_values(GroupPolicyDefinitionValue)),
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
        writer.write_collection_of_object_values("added", self.added)
        writer.write_collection_of_primitive_values("deletedIds", self.deleted_ids)
        writer.write_collection_of_object_values("updated", self.updated)
        writer.write_additional_data_value(self.additional_data)
    


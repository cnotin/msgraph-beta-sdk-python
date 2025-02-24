from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_audit_property import CloudPcAuditProperty

@dataclass
class CloudPcAuditResource(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The resource entity display name.
    display_name: Optional[str] = None
    # A list of modified properties.
    modified_properties: Optional[List[CloudPcAuditProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the audit resource.
    resource_id: Optional[str] = None
    # The type of the audit resource.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcAuditResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAuditResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAuditResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_audit_property import CloudPcAuditProperty

        from .cloud_pc_audit_property import CloudPcAuditProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(CloudPcAuditProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    


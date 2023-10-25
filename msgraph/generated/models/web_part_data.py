from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json import Json
    from .server_processed_content import ServerProcessedContent

@dataclass
class WebPartData(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Audience information of the web part. By using this property, specific content is prioritized to specific audiences.
    audiences: Optional[List[str]] = None
    # Data version of the web part. The value is defined by the web part developer. Different dataVersions usually refers to a different property structure.
    data_version: Optional[str] = None
    # Description of the web part.
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Properties bag of the web part.
    properties: Optional[Json] = None
    # Contains collections of data that can be processed by server side services like search index and link fixup.
    server_processed_content: Optional[ServerProcessedContent] = None
    # Title of the web part.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebPartData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebPartData
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WebPartData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .json import Json
        from .server_processed_content import ServerProcessedContent

        from .json import Json
        from .server_processed_content import ServerProcessedContent

        fields: Dict[str, Callable[[Any], None]] = {
            "audiences": lambda n : setattr(self, 'audiences', n.get_collection_of_primitive_values(str)),
            "dataVersion": lambda n : setattr(self, 'data_version', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(Json)),
            "serverProcessedContent": lambda n : setattr(self, 'server_processed_content', n.get_object_value(ServerProcessedContent)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("audiences", self.audiences)
        writer.write_str_value("dataVersion", self.data_version)
        writer.write_str_value("description", self.description)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("properties", self.properties)
        writer.write_object_value("serverProcessedContent", self.server_processed_content)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    


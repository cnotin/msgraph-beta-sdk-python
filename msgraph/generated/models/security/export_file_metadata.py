from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ExportFileMetadata(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The downloadUrl property
    download_url: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The size property
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExportFileMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportFileMetadata
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExportFileMetadata()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    


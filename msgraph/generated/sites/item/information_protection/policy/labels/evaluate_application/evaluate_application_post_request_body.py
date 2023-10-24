from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.content_info import ContentInfo
    from .......models.labeling_options import LabelingOptions

@dataclass
class EvaluateApplicationPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The contentInfo property
    content_info: Optional[ContentInfo] = None
    # The labelingOptions property
    labeling_options: Optional[LabelingOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateApplicationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateApplicationPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateApplicationPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models.content_info import ContentInfo
        from .......models.labeling_options import LabelingOptions

        from .......models.content_info import ContentInfo
        from .......models.labeling_options import LabelingOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(ContentInfo)),
            "labelingOptions": lambda n : setattr(self, 'labeling_options', n.get_object_value(LabelingOptions)),
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
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_object_value("labelingOptions", self.labeling_options)
        writer.write_additional_data_value(self.additional_data)
    


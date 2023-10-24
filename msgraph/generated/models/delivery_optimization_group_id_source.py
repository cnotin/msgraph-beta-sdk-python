from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_group_id_custom import DeliveryOptimizationGroupIdCustom
    from .delivery_optimization_group_id_source_options import DeliveryOptimizationGroupIdSourceOptions

@dataclass
class DeliveryOptimizationGroupIdSource(AdditionalDataHolder, BackedModel, Parsable):
    """
    GroupId Support Types
    """
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationGroupIdSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationGroupIdSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationGroupIdCustom".casefold():
            from .delivery_optimization_group_id_custom import DeliveryOptimizationGroupIdCustom

            return DeliveryOptimizationGroupIdCustom()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationGroupIdSourceOptions".casefold():
            from .delivery_optimization_group_id_source_options import DeliveryOptimizationGroupIdSourceOptions

            return DeliveryOptimizationGroupIdSourceOptions()
        return DeliveryOptimizationGroupIdSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_group_id_custom import DeliveryOptimizationGroupIdCustom
        from .delivery_optimization_group_id_source_options import DeliveryOptimizationGroupIdSourceOptions

        from .delivery_optimization_group_id_custom import DeliveryOptimizationGroupIdCustom
        from .delivery_optimization_group_id_source_options import DeliveryOptimizationGroupIdSourceOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


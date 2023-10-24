from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EvaluateDynamicMembershipPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The memberId property
    member_id: Optional[str] = None
    # The membershipRule property
    membership_rule: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateDynamicMembershipPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateDynamicMembershipPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateDynamicMembershipPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "memberId": lambda n : setattr(self, 'member_id', n.get_str_value()),
            "membershipRule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
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
        writer.write_str_value("memberId", self.member_id)
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_additional_data_value(self.additional_data)
    


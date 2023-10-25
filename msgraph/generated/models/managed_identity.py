from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .msi_type import MsiType

@dataclass
class ManagedIdentity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The ARM resource ID of the Azure resource associated with the managed identity used for sign in.
    associated_resource_id: Optional[str] = None
    # The unique ID of the federated token.
    federated_token_id: Optional[str] = None
    # The issuer of the federated token.
    federated_token_issuer: Optional[str] = None
    # The possible values are: none, userAssigned, systemAssigned, unknownFutureValue.
    msi_type: Optional[MsiType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .msi_type import MsiType

        from .msi_type import MsiType

        fields: Dict[str, Callable[[Any], None]] = {
            "associatedResourceId": lambda n : setattr(self, 'associated_resource_id', n.get_str_value()),
            "federatedTokenId": lambda n : setattr(self, 'federated_token_id', n.get_str_value()),
            "federatedTokenIssuer": lambda n : setattr(self, 'federated_token_issuer', n.get_str_value()),
            "msiType": lambda n : setattr(self, 'msi_type', n.get_enum_value(MsiType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("associatedResourceId", self.associated_resource_id)
        writer.write_str_value("federatedTokenId", self.federated_token_id)
        writer.write_str_value("federatedTokenIssuer", self.federated_token_issuer)
        writer.write_enum_value("msiType", self.msi_type)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


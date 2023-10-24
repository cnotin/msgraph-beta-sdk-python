from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RedirectUriSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Identifies the specific URI within the redirectURIs collection in SAML SSO flows. Defaults to null. The index is unique across all the redirectUris for the application.
    index: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the URI that tokens are sent to.
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedirectUriSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectUriSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RedirectUriSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_int_value("index", self.index)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("uri", self.uri)
        writer.write_additional_data_value(self.additional_data)
    


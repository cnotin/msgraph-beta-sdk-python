from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class MessageSecurityState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The connectingIP property
    connecting_i_p: Optional[str] = None
    # The deliveryAction property
    delivery_action: Optional[str] = None
    # The deliveryLocation property
    delivery_location: Optional[str] = None
    # The directionality property
    directionality: Optional[str] = None
    # The internetMessageId property
    internet_message_id: Optional[str] = None
    # The messageFingerprint property
    message_fingerprint: Optional[str] = None
    # The messageReceivedDateTime property
    message_received_date_time: Optional[datetime.datetime] = None
    # The messageSubject property
    message_subject: Optional[str] = None
    # The networkMessageId property
    network_message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageSecurityState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MessageSecurityState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "connectingIP": lambda n : setattr(self, 'connecting_i_p', n.get_str_value()),
            "deliveryAction": lambda n : setattr(self, 'delivery_action', n.get_str_value()),
            "deliveryLocation": lambda n : setattr(self, 'delivery_location', n.get_str_value()),
            "directionality": lambda n : setattr(self, 'directionality', n.get_str_value()),
            "internetMessageId": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "messageFingerprint": lambda n : setattr(self, 'message_fingerprint', n.get_str_value()),
            "messageReceivedDateTime": lambda n : setattr(self, 'message_received_date_time', n.get_datetime_value()),
            "messageSubject": lambda n : setattr(self, 'message_subject', n.get_str_value()),
            "networkMessageId": lambda n : setattr(self, 'network_message_id', n.get_str_value()),
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
        writer.write_str_value("connectingIP", self.connecting_i_p)
        writer.write_str_value("deliveryAction", self.delivery_action)
        writer.write_str_value("deliveryLocation", self.delivery_location)
        writer.write_str_value("directionality", self.directionality)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_str_value("messageFingerprint", self.message_fingerprint)
        writer.write_datetime_value("messageReceivedDateTime", self.message_received_date_time)
        writer.write_str_value("messageSubject", self.message_subject)
        writer.write_str_value("networkMessageId", self.network_message_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


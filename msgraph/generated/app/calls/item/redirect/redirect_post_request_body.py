from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.call_disposition import CallDisposition
    from .....models.invitation_participant_info import InvitationParticipantInfo

@dataclass
class RedirectPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The callbackUri property
    callback_uri: Optional[str] = None
    # The maskCallee property
    mask_callee: Optional[bool] = None
    # The maskCaller property
    mask_caller: Optional[bool] = None
    # The targetDisposition property
    target_disposition: Optional[CallDisposition] = None
    # The targets property
    targets: Optional[List[InvitationParticipantInfo]] = None
    # The timeout property
    timeout: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedirectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RedirectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.call_disposition import CallDisposition
        from .....models.invitation_participant_info import InvitationParticipantInfo

        from .....models.call_disposition import CallDisposition
        from .....models.invitation_participant_info import InvitationParticipantInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "maskCallee": lambda n : setattr(self, 'mask_callee', n.get_bool_value()),
            "maskCaller": lambda n : setattr(self, 'mask_caller', n.get_bool_value()),
            "targetDisposition": lambda n : setattr(self, 'target_disposition', n.get_enum_value(CallDisposition)),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(InvitationParticipantInfo)),
            "timeout": lambda n : setattr(self, 'timeout', n.get_int_value()),
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
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_bool_value("maskCallee", self.mask_callee)
        writer.write_bool_value("maskCaller", self.mask_caller)
        writer.write_enum_value("targetDisposition", self.target_disposition)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_int_value("timeout", self.timeout)
        writer.write_additional_data_value(self.additional_data)
    


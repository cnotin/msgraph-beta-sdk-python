from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet
    from .teamwork_user_identity import TeamworkUserIdentity

from .event_message_detail import EventMessageDetail

@dataclass
class MembersAddedEventMessageDetail(EventMessageDetail):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.membersAddedEventMessageDetail"
    # Initiator of the event.
    initiator: Optional[IdentitySet] = None
    # List of members added.
    members: Optional[List[TeamworkUserIdentity]] = None
    # The timestamp denoting how far back a conversation's history is shared with the conversation members.
    visible_history_start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MembersAddedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MembersAddedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MembersAddedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet
        from .teamwork_user_identity import TeamworkUserIdentity

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet
        from .teamwork_user_identity import TeamworkUserIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(TeamworkUserIdentity)),
            "visibleHistoryStartDateTime": lambda n : setattr(self, 'visible_history_start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("initiator", self.initiator)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_datetime_value("visibleHistoryStartDateTime", self.visible_history_start_date_time)
    


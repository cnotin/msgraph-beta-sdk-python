from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class CallRecording(Entity):
    # The content of the recording. Read-only.
    content: Optional[bytes] = None
    # Date and time at which the recording was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the onlineMeeting related to this recording. Read-only.
    meeting_id: Optional[str] = None
    # The identity information of the organizer of the onlineMeeting related to this recording. Read-only.
    meeting_organizer: Optional[IdentitySet] = None
    # The unique identifier of the organizer of the onlineMeeting related to this recording. Read-only.
    meeting_organizer_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL which can be used to access the content of the recording. Read-only.
    recording_content_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRecording:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallRecording
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CallRecording()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet

        from .entity import Entity
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "meetingId": lambda n : setattr(self, 'meeting_id', n.get_str_value()),
            "meetingOrganizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(IdentitySet)),
            "meetingOrganizerId": lambda n : setattr(self, 'meeting_organizer_id', n.get_str_value()),
            "recordingContentUrl": lambda n : setattr(self, 'recording_content_url', n.get_str_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("meetingId", self.meeting_id)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
        writer.write_str_value("meetingOrganizerId", self.meeting_organizer_id)
        writer.write_str_value("recordingContentUrl", self.recording_content_url)
    


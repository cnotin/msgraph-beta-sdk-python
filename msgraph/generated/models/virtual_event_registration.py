from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
    from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
    from .virtual_event_session import VirtualEventSession

from .entity import Entity

@dataclass
class VirtualEventRegistration(Entity):
    # The cancelationDateTime property
    cancelation_date_time: Optional[datetime.datetime] = None
    # The email property
    email: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The registrationDateTime property
    registration_date_time: Optional[datetime.datetime] = None
    # The registrationQuestionAnswers property
    registration_question_answers: Optional[List[VirtualEventRegistrationQuestionAnswer]] = None
    # The sessions property
    sessions: Optional[List[VirtualEventSession]] = None
    # The status property
    status: Optional[VirtualEventAttendeeRegistrationStatus] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
        from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
        from .virtual_event_session import VirtualEventSession

        from .entity import Entity
        from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
        from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
        from .virtual_event_session import VirtualEventSession

        fields: Dict[str, Callable[[Any], None]] = {
            "cancelationDateTime": lambda n : setattr(self, 'cancelation_date_time', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "registrationQuestionAnswers": lambda n : setattr(self, 'registration_question_answers', n.get_collection_of_object_values(VirtualEventRegistrationQuestionAnswer)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(VirtualEventSession)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(VirtualEventAttendeeRegistrationStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_datetime_value("cancelationDateTime", self.cancelation_date_time)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_collection_of_object_values("registrationQuestionAnswers", self.registration_question_answers)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .communications_user_identity import CommunicationsUserIdentity
    from .entity import Entity
    from .virtual_event_presenter_details import VirtualEventPresenterDetails
    from .virtual_event_session import VirtualEventSession

from .entity import Entity

@dataclass
class VirtualEventPresenter(Entity):
    # Email address of the presenter.
    email: Optional[str] = None
    # Identity information of the presenter.
    identity: Optional[CommunicationsUserIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Other detail information of the presenter.
    presenter_details: Optional[VirtualEventPresenterDetails] = None
    # The profilePhoto property
    profile_photo: Optional[bytes] = None
    # The sessions property
    sessions: Optional[List[VirtualEventSession]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventPresenter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenter
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventPresenter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .communications_user_identity import CommunicationsUserIdentity
        from .entity import Entity
        from .virtual_event_presenter_details import VirtualEventPresenterDetails
        from .virtual_event_session import VirtualEventSession

        from .communications_user_identity import CommunicationsUserIdentity
        from .entity import Entity
        from .virtual_event_presenter_details import VirtualEventPresenterDetails
        from .virtual_event_session import VirtualEventSession

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(CommunicationsUserIdentity)),
            "presenterDetails": lambda n : setattr(self, 'presenter_details', n.get_object_value(VirtualEventPresenterDetails)),
            "profilePhoto": lambda n : setattr(self, 'profile_photo', n.get_bytes_value()),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(VirtualEventSession)),
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
        writer.write_str_value("email", self.email)
        writer.write_object_value("identity", self.identity)
        writer.write_object_value("presenterDetails", self.presenter_details)
        writer.write_bytes_value("profilePhoto", self.profile_photo)
        writer.write_collection_of_object_values("sessions", self.sessions)
    


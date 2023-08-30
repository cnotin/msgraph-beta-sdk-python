from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity
    from .teamwork_application_identity_type import TeamworkApplicationIdentityType

from .identity import Identity

@dataclass
class TeamworkApplicationIdentity(Identity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.teamworkApplicationIdentity"
    # Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, and outgoingWebhook.
    application_identity_type: Optional[TeamworkApplicationIdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkApplicationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkApplicationIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkApplicationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity
        from .teamwork_application_identity_type import TeamworkApplicationIdentityType

        from .identity import Identity
        from .teamwork_application_identity_type import TeamworkApplicationIdentityType

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationIdentityType": lambda n : setattr(self, 'application_identity_type', n.get_enum_value(TeamworkApplicationIdentityType)),
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
        writer.write_enum_value("applicationIdentityType", self.application_identity_type)
    


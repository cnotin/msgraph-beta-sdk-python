from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_identity import AwsIdentity
    from .aws_role import AwsRole

from .aws_identity import AwsIdentity

@dataclass
class AwsUser(AwsIdentity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsUser"
    # The assumableRoles property
    assumable_roles: Optional[List[AwsRole]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AwsUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsUser
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AwsUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_identity import AwsIdentity
        from .aws_role import AwsRole

        from .aws_identity import AwsIdentity
        from .aws_role import AwsRole

        fields: Dict[str, Callable[[Any], None]] = {
            "assumableRoles": lambda n : setattr(self, 'assumable_roles', n.get_collection_of_object_values(AwsRole)),
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
        writer.write_collection_of_object_values("assumableRoles", self.assumable_roles)
    


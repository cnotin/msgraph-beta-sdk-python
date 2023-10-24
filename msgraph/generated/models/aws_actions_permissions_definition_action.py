from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
    from .aws_statement import AwsStatement

from .aws_permissions_definition_action import AwsPermissionsDefinitionAction

@dataclass
class AwsActionsPermissionsDefinitionAction(AwsPermissionsDefinitionAction):
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.awsActionsPermissionsDefinitionAction"
    # The assignToRoleId property
    assign_to_role_id: Optional[str] = None
    # The statements property
    statements: Optional[List[AwsStatement]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AwsActionsPermissionsDefinitionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsActionsPermissionsDefinitionAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AwsActionsPermissionsDefinitionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .aws_statement import AwsStatement

        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .aws_statement import AwsStatement

        fields: Dict[str, Callable[[Any], None]] = {
            "assignToRoleId": lambda n : setattr(self, 'assign_to_role_id', n.get_str_value()),
            "statements": lambda n : setattr(self, 'statements', n.get_collection_of_object_values(AwsStatement)),
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
        writer.write_str_value("assignToRoleId", self.assign_to_role_id)
        writer.write_collection_of_object_values("statements", self.statements)
    


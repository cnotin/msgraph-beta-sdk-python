from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_set_item = lazy_import('msgraph.generated.models.policy_set_item')

class IosLobAppProvisioningConfigurationPolicySetItem(policy_set_item.PolicySetItem):
    def __init__(self,) -> None:
        """
        Instantiates a new IosLobAppProvisioningConfigurationPolicySetItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosLobAppProvisioningConfigurationPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosLobAppProvisioningConfigurationPolicySetItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosLobAppProvisioningConfigurationPolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UpdateDevicePropertiesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The addressableUserName property
    addressable_user_name: Optional[str] = None
    # The deviceAccountPassword property
    device_account_password: Optional[str] = None
    # The deviceAccountUpn property
    device_account_upn: Optional[str] = None
    # The deviceFriendlyName property
    device_friendly_name: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The groupTag property
    group_tag: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateDevicePropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateDevicePropertiesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateDevicePropertiesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "addressableUserName": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "deviceAccountPassword": lambda n : setattr(self, 'device_account_password', n.get_str_value()),
            "deviceAccountUpn": lambda n : setattr(self, 'device_account_upn', n.get_str_value()),
            "deviceFriendlyName": lambda n : setattr(self, 'device_friendly_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupTag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("addressableUserName", self.addressable_user_name)
        writer.write_str_value("deviceAccountPassword", self.device_account_password)
        writer.write_str_value("deviceAccountUpn", self.device_account_upn)
        writer.write_str_value("deviceFriendlyName", self.device_friendly_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    


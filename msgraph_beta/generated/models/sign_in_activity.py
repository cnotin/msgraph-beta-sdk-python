from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SignInActivity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The last non-interactive sign-in date for a specific user. You can use this field to calculate the last time a client attempted to sign into the directory the directory on behalf of a user. Because some users may use clients to access tenant resources rather than signing into your tenant directly, you can use the non-interactive sign-in date to along with lastSignInDateTime to identify inactive users. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is: '2014-01-01T00:00:00Z'. Microsoft Entra ID maintains non-interactive sign-ins going back to May 2020. For more information about using the value of this property, see Manage inactive user accounts in Microsoft Entra ID.
    last_non_interactive_sign_in_date_time: Optional[datetime.datetime] = None
    # Request identifier of the last non-interactive sign-in performed by this user.
    last_non_interactive_sign_in_request_id: Optional[str] = None
    # The last interactive sign-in date and time for a specific user. You can use this field to calculate the last time a user attempted to sign into the directory the directory with an interactive authentication method. This field can be used to build reports, such as inactive users. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is: '2014-01-01T00:00:00Z'. Microsoft Entra ID maintains interactive sign-ins going back to April 2020. For more information about using the value of this property, see Manage inactive user accounts in Microsoft Entra ID.
    last_sign_in_date_time: Optional[datetime.datetime] = None
    # Request identifier of the last interactive sign-in performed by this user.
    last_sign_in_request_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SignInActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "lastNonInteractiveSignInDateTime": lambda n : setattr(self, 'last_non_interactive_sign_in_date_time', n.get_datetime_value()),
            "lastNonInteractiveSignInRequestId": lambda n : setattr(self, 'last_non_interactive_sign_in_request_id', n.get_str_value()),
            "lastSignInDateTime": lambda n : setattr(self, 'last_sign_in_date_time', n.get_datetime_value()),
            "lastSignInRequestId": lambda n : setattr(self, 'last_sign_in_request_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_datetime_value("lastNonInteractiveSignInDateTime", self.last_non_interactive_sign_in_date_time)
        writer.write_str_value("lastNonInteractiveSignInRequestId", self.last_non_interactive_sign_in_request_id)
        writer.write_datetime_value("lastSignInDateTime", self.last_sign_in_date_time)
        writer.write_str_value("lastSignInRequestId", self.last_sign_in_request_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


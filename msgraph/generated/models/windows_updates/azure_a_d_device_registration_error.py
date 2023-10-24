from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_a_d_device_registration_error_reason import AzureADDeviceRegistrationErrorReason
    from .updatable_asset_error import UpdatableAssetError

from .updatable_asset_error import UpdatableAssetError

@dataclass
class AzureADDeviceRegistrationError(UpdatableAssetError):
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.windowsUpdates.azureADDeviceRegistrationError"
    # The reason property
    reason: Optional[AzureADDeviceRegistrationErrorReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureADDeviceRegistrationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureADDeviceRegistrationError
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AzureADDeviceRegistrationError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .azure_a_d_device_registration_error_reason import AzureADDeviceRegistrationErrorReason
        from .updatable_asset_error import UpdatableAssetError

        from .azure_a_d_device_registration_error_reason import AzureADDeviceRegistrationErrorReason
        from .updatable_asset_error import UpdatableAssetError

        fields: Dict[str, Callable[[Any], None]] = {
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(AzureADDeviceRegistrationErrorReason)),
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
        writer.write_enum_value("reason", self.reason)
    


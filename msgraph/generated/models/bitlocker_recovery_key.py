from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .volume_type import VolumeType

from .entity import Entity

@dataclass
class BitlockerRecoveryKey(Entity):
    # The date and time when the key was originally backed up to Microsoft Entra ID.
    created_date_time: Optional[datetime.datetime] = None
    # ID of the device the BitLocker key is originally backed up from.
    device_id: Optional[str] = None
    # The BitLocker recovery key.
    key: Optional[str] = None
    # The OdataType property
    OdataType: Optional[str] = None
    # Indicates the type of volume the BitLocker key is associated with. Possible values are: operatingSystemVolume, fixedDataVolume, removableDataVolume, unknownFutureValue.
    volume_type: Optional[VolumeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitlockerRecoveryKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BitlockerRecoveryKey
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BitlockerRecoveryKey()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .volume_type import VolumeType

        from .entity import Entity
        from .volume_type import VolumeType

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "volumeType": lambda n : setattr(self, 'volume_type', n.get_enum_value(VolumeType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("key", self.key)
        writer.write_enum_value("volumeType", self.volume_type)
    


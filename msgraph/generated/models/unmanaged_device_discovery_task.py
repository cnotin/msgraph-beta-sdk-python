from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_app_management_task import DeviceAppManagementTask
    from .unmanaged_device import UnmanagedDevice

from .device_app_management_task import DeviceAppManagementTask

@dataclass
class UnmanagedDeviceDiscoveryTask(DeviceAppManagementTask):
    """
    This task derived type represents a list of unmanaged devices discovered in the network.
    """
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.unmanagedDeviceDiscoveryTask"
    # Unmanaged devices discovered in the network.
    unmanaged_devices: Optional[List[UnmanagedDevice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnmanagedDeviceDiscoveryTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnmanagedDeviceDiscoveryTask
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnmanagedDeviceDiscoveryTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_app_management_task import DeviceAppManagementTask
        from .unmanaged_device import UnmanagedDevice

        from .device_app_management_task import DeviceAppManagementTask
        from .unmanaged_device import UnmanagedDevice

        fields: Dict[str, Callable[[Any], None]] = {
            "unmanagedDevices": lambda n : setattr(self, 'unmanaged_devices', n.get_collection_of_object_values(UnmanagedDevice)),
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
        writer.write_collection_of_object_values("unmanagedDevices", self.unmanaged_devices)
    


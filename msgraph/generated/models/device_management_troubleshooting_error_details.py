from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_troubleshooting_error_resource import DeviceManagementTroubleshootingErrorResource

@dataclass
class DeviceManagementTroubleshootingErrorDetails(AdditionalDataHolder, BackedModel, Parsable):
    """
    Object containing detailed information about the error and its remediation.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Not yet documented
    context: Optional[str] = None
    # Not yet documented
    failure: Optional[str] = None
    # The detailed description of what went wrong.
    failure_details: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The detailed description of how to remediate this issue.
    remediation: Optional[str] = None
    # Links to helpful documentation about this failure.
    resources: Optional[List[DeviceManagementTroubleshootingErrorResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTroubleshootingErrorDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTroubleshootingErrorDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementTroubleshootingErrorDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_troubleshooting_error_resource import DeviceManagementTroubleshootingErrorResource

        from .device_management_troubleshooting_error_resource import DeviceManagementTroubleshootingErrorResource

        fields: Dict[str, Callable[[Any], None]] = {
            "context": lambda n : setattr(self, 'context', n.get_str_value()),
            "failure": lambda n : setattr(self, 'failure', n.get_str_value()),
            "failureDetails": lambda n : setattr(self, 'failure_details', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediation": lambda n : setattr(self, 'remediation', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(DeviceManagementTroubleshootingErrorResource)),
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
        writer.write_str_value("context", self.context)
        writer.write_str_value("failure", self.failure)
        writer.write_str_value("failureDetails", self.failure_details)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("remediation", self.remediation)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import msi_type

class ManagedIdentity(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new managedIdentity and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ARM resource ID of the Azure resource associated with the managed identity used for sign in.
        self._associated_resource_id: Optional[str] = None
        # The possible values are: none, userAssigned, systemAssigned, unknownFutureValue.
        self._msi_type: Optional[msi_type.MsiType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def associated_resource_id(self,) -> Optional[str]:
        """
        Gets the associatedResourceId property value. The ARM resource ID of the Azure resource associated with the managed identity used for sign in.
        Returns: Optional[str]
        """
        return self._associated_resource_id
    
    @associated_resource_id.setter
    def associated_resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the associatedResourceId property value. The ARM resource ID of the Azure resource associated with the managed identity used for sign in.
        Args:
            value: Value to set for the associated_resource_id property.
        """
        self._associated_resource_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import msi_type

        fields: Dict[str, Callable[[Any], None]] = {
            "associatedResourceId": lambda n : setattr(self, 'associated_resource_id', n.get_str_value()),
            "msiType": lambda n : setattr(self, 'msi_type', n.get_enum_value(msi_type.MsiType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def msi_type(self,) -> Optional[msi_type.MsiType]:
        """
        Gets the msiType property value. The possible values are: none, userAssigned, systemAssigned, unknownFutureValue.
        Returns: Optional[msi_type.MsiType]
        """
        return self._msi_type
    
    @msi_type.setter
    def msi_type(self,value: Optional[msi_type.MsiType] = None) -> None:
        """
        Sets the msiType property value. The possible values are: none, userAssigned, systemAssigned, unknownFutureValue.
        Args:
            value: Value to set for the msi_type property.
        """
        self._msi_type = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("associatedResourceId", self.associated_resource_id)
        writer.write_enum_value("msiType", self.msi_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


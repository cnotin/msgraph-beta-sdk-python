from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

registration_status_type = lazy_import('msgraph.generated.models.registration_status_type')

class UserRegistrationCount(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new userRegistrationCount and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Provides the registration count for your tenant.
        self._registration_count: Optional[int] = None
        # The registrationStatus property
        self._registration_status: Optional[registration_status_type.RegistrationStatusType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserRegistrationCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationCount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserRegistrationCount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "registration_count": lambda n : setattr(self, 'registration_count', n.get_int_value()),
            "registration_status": lambda n : setattr(self, 'registration_status', n.get_enum_value(registration_status_type.RegistrationStatusType)),
        }
        return fields
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def registration_count(self,) -> Optional[int]:
        """
        Gets the registrationCount property value. Provides the registration count for your tenant.
        Returns: Optional[int]
        """
        return self._registration_count
    
    @registration_count.setter
    def registration_count(self,value: Optional[int] = None) -> None:
        """
        Sets the registrationCount property value. Provides the registration count for your tenant.
        Args:
            value: Value to set for the registrationCount property.
        """
        self._registration_count = value
    
    @property
    def registration_status(self,) -> Optional[registration_status_type.RegistrationStatusType]:
        """
        Gets the registrationStatus property value. The registrationStatus property
        Returns: Optional[registration_status_type.RegistrationStatusType]
        """
        return self._registration_status
    
    @registration_status.setter
    def registration_status(self,value: Optional[registration_status_type.RegistrationStatusType] = None) -> None:
        """
        Sets the registrationStatus property value. The registrationStatus property
        Args:
            value: Value to set for the registrationStatus property.
        """
        self._registration_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("registrationCount", self.registration_count)
        writer.write_enum_value("registrationStatus", self.registration_status)
        writer.write_additional_data_value(self.additional_data)
    


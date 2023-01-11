from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

credential = lazy_import('msgraph.generated.models.credential')

class UpdatePasswordSingleSignOnCredentialsPostRequestBody(AdditionalDataHolder, Parsable):
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
        Instantiates a new updatePasswordSingleSignOnCredentialsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The credentials property
        self._credentials: Optional[List[credential.Credential]] = None
        # The id property
        self._id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePasswordSingleSignOnCredentialsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePasswordSingleSignOnCredentialsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdatePasswordSingleSignOnCredentialsPostRequestBody()
    
    @property
    def credentials(self,) -> Optional[List[credential.Credential]]:
        """
        Gets the credentials property value. The credentials property
        Returns: Optional[List[credential.Credential]]
        """
        return self._credentials
    
    @credentials.setter
    def credentials(self,value: Optional[List[credential.Credential]] = None) -> None:
        """
        Sets the credentials property value. The credentials property
        Args:
            value: Value to set for the credentials property.
        """
        self._credentials = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "credentials": lambda n : setattr(self, 'credentials', n.get_collection_of_object_values(credential.Credential)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("credentials", self.credentials)
        writer.write_str_value("id", self.id)
        writer.write_additional_data_value(self.additional_data)
    


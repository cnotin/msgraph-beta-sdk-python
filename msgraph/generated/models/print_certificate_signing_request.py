from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class PrintCertificateSigningRequest(AdditionalDataHolder, Parsable):
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
        Instantiates a new printCertificateSigningRequest and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A base64-encoded pkcs10 certificate request. Read-only.
        self._content: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The base64-encoded public portion of an asymmetric key that is generated by the client. Read-only.
        self._transport_key: Optional[str] = None
    
    @property
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. A base64-encoded pkcs10 certificate request. Read-only.
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. A base64-encoded pkcs10 certificate request. Read-only.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintCertificateSigningRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintCertificateSigningRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintCertificateSigningRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "transport_key": lambda n : setattr(self, 'transport_key', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("content", self.content)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("transportKey", self.transport_key)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def transport_key(self,) -> Optional[str]:
        """
        Gets the transportKey property value. The base64-encoded public portion of an asymmetric key that is generated by the client. Read-only.
        Returns: Optional[str]
        """
        return self._transport_key
    
    @transport_key.setter
    def transport_key(self,value: Optional[str] = None) -> None:
        """
        Sets the transportKey property value. The base64-encoded public portion of an asymmetric key that is generated by the client. Read-only.
        Args:
            value: Value to set for the transportKey property.
        """
        self._transport_key = value
    


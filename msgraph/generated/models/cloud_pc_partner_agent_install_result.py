from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import cloud_pc_partner_agent_install_status, cloud_pc_partner_agent_name

class CloudPcPartnerAgentInstallResult(AdditionalDataHolder, Parsable):
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
        Instantiates a new cloudPcPartnerAgentInstallResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The installStatus property
        self._install_status: Optional[cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus] = None
        # The isThirdPartyPartner property
        self._is_third_party_partner: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The partnerAgentName property
        self._partner_agent_name: Optional[cloud_pc_partner_agent_name.CloudPcPartnerAgentName] = None
        # The retriable property
        self._retriable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcPartnerAgentInstallResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcPartnerAgentInstallResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcPartnerAgentInstallResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "install_status": lambda n : setattr(self, 'install_status', n.get_enum_value(cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus)),
            "is_third_party_partner": lambda n : setattr(self, 'is_third_party_partner', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partner_agent_name": lambda n : setattr(self, 'partner_agent_name', n.get_enum_value(cloud_pc_partner_agent_name.CloudPcPartnerAgentName)),
            "retriable": lambda n : setattr(self, 'retriable', n.get_bool_value()),
        }
        return fields
    
    @property
    def install_status(self,) -> Optional[cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus]:
        """
        Gets the installStatus property value. The installStatus property
        Returns: Optional[cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus]
        """
        return self._install_status
    
    @install_status.setter
    def install_status(self,value: Optional[cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus] = None) -> None:
        """
        Sets the installStatus property value. The installStatus property
        Args:
            value: Value to set for the installStatus property.
        """
        self._install_status = value
    
    @property
    def is_third_party_partner(self,) -> Optional[bool]:
        """
        Gets the isThirdPartyPartner property value. The isThirdPartyPartner property
        Returns: Optional[bool]
        """
        return self._is_third_party_partner
    
    @is_third_party_partner.setter
    def is_third_party_partner(self,value: Optional[bool] = None) -> None:
        """
        Sets the isThirdPartyPartner property value. The isThirdPartyPartner property
        Args:
            value: Value to set for the isThirdPartyPartner property.
        """
        self._is_third_party_partner = value
    
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
    def partner_agent_name(self,) -> Optional[cloud_pc_partner_agent_name.CloudPcPartnerAgentName]:
        """
        Gets the partnerAgentName property value. The partnerAgentName property
        Returns: Optional[cloud_pc_partner_agent_name.CloudPcPartnerAgentName]
        """
        return self._partner_agent_name
    
    @partner_agent_name.setter
    def partner_agent_name(self,value: Optional[cloud_pc_partner_agent_name.CloudPcPartnerAgentName] = None) -> None:
        """
        Sets the partnerAgentName property value. The partnerAgentName property
        Args:
            value: Value to set for the partnerAgentName property.
        """
        self._partner_agent_name = value
    
    @property
    def retriable(self,) -> Optional[bool]:
        """
        Gets the retriable property value. The retriable property
        Returns: Optional[bool]
        """
        return self._retriable
    
    @retriable.setter
    def retriable(self,value: Optional[bool] = None) -> None:
        """
        Sets the retriable property value. The retriable property
        Args:
            value: Value to set for the retriable property.
        """
        self._retriable = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("installStatus", self.install_status)
        writer.write_bool_value("isThirdPartyPartner", self.is_third_party_partner)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("partnerAgentName", self.partner_agent_name)
        writer.write_bool_value("retriable", self.retriable)
        writer.write_additional_data_value(self.additional_data)
    


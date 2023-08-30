from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_certificate_access_type import AndroidDeviceOwnerCertificateAccessType
    from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
    from .android_device_owner_silent_certificate_access import AndroidDeviceOwnerSilentCertificateAccess
    from .intended_purpose import IntendedPurpose
    from .managed_device_certificate_state import ManagedDeviceCertificateState

from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase

@dataclass
class AndroidDeviceOwnerImportedPFXCertificateProfile(AndroidDeviceOwnerCertificateProfileBase):
    """
    Android Device Owner PFX Import certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile"
    # Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
    certificate_access_type: Optional[AndroidDeviceOwnerCertificateAccessType] = None
    # PFX Import Options.
    intended_purpose: Optional[IntendedPurpose] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[ManagedDeviceCertificateState]] = None
    # Certificate access information. This collection can contain a maximum of 50 elements.
    silent_certificate_access_details: Optional[List[AndroidDeviceOwnerSilentCertificateAccess]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerImportedPFXCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_certificate_access_type import AndroidDeviceOwnerCertificateAccessType
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_silent_certificate_access import AndroidDeviceOwnerSilentCertificateAccess
        from .intended_purpose import IntendedPurpose
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        from .android_device_owner_certificate_access_type import AndroidDeviceOwnerCertificateAccessType
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_silent_certificate_access import AndroidDeviceOwnerSilentCertificateAccess
        from .intended_purpose import IntendedPurpose
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateAccessType": lambda n : setattr(self, 'certificate_access_type', n.get_enum_value(AndroidDeviceOwnerCertificateAccessType)),
            "intendedPurpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(IntendedPurpose)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
            "silentCertificateAccessDetails": lambda n : setattr(self, 'silent_certificate_access_details', n.get_collection_of_object_values(AndroidDeviceOwnerSilentCertificateAccess)),
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
        writer.write_enum_value("certificateAccessType", self.certificate_access_type)
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_collection_of_object_values("silentCertificateAccessDetails", self.silent_certificate_access_details)
    


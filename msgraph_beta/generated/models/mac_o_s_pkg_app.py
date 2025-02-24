from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_app_script import MacOSAppScript
    from .mac_o_s_included_app import MacOSIncludedApp
    from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
    from .mobile_lob_app import MobileLobApp

from .mobile_lob_app import MobileLobApp

@dataclass
class MacOSPkgApp(MobileLobApp):
    """
    Contains properties and inherited properties for the MacOSPkgApp.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSPkgApp"
    # A value indicating whether the app's version will be used to detect the app after it is installed on a device. Set this to true for apps that use a self-update feature. Set this to false to install the app when it is not already installed on the device, or if the deploying app's version number does not match the version that's already installed on the device. The default value is false.
    ignore_version_detection: Optional[bool] = None
    # The list of apps expected to be installed by the .pkg.
    included_apps: Optional[List[MacOSIncludedApp]] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[MacOSMinimumOperatingSystem] = None
    # ComplexType macOSAppScript the contains the post-install script for the app. This will execute on the macOS device after the app is installed.
    post_install_script: Optional[MacOSAppScript] = None
    # ComplexType macOSAppScript the contains the post-install script for the app. This will execute on the macOS device after the app is installed.
    pre_install_script: Optional[MacOSAppScript] = None
    # The primary CFBundleIdentifier of the .pkg.
    primary_bundle_id: Optional[str] = None
    # The primary CFBundleVersion of the .pkg.
    primary_bundle_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSPkgApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSPkgApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSPkgApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_app_script import MacOSAppScript
        from .mac_o_s_included_app import MacOSIncludedApp
        from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        from .mac_o_s_app_script import MacOSAppScript
        from .mac_o_s_included_app import MacOSIncludedApp
        from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        fields: Dict[str, Callable[[Any], None]] = {
            "ignoreVersionDetection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "includedApps": lambda n : setattr(self, 'included_apps', n.get_collection_of_object_values(MacOSIncludedApp)),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(MacOSMinimumOperatingSystem)),
            "postInstallScript": lambda n : setattr(self, 'post_install_script', n.get_object_value(MacOSAppScript)),
            "preInstallScript": lambda n : setattr(self, 'pre_install_script', n.get_object_value(MacOSAppScript)),
            "primaryBundleId": lambda n : setattr(self, 'primary_bundle_id', n.get_str_value()),
            "primaryBundleVersion": lambda n : setattr(self, 'primary_bundle_version', n.get_str_value()),
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
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_collection_of_object_values("includedApps", self.included_apps)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_object_value("postInstallScript", self.post_install_script)
        writer.write_object_value("preInstallScript", self.pre_install_script)
        writer.write_str_value("primaryBundleId", self.primary_bundle_id)
        writer.write_str_value("primaryBundleVersion", self.primary_bundle_version)
    


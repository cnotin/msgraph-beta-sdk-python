from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
    from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcUserSetting(Entity):
    # Represents the set of Microsoft 365 groups and security groups in Microsoft Entra ID that have cloudPCUserSetting assigned. Returned only on $expand. For an example, see Get cloudPcUserSettingample.
    assignments: Optional[List[CloudPcUserSettingAssignment]] = None
    # The date and time the setting was created. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
    created_date_time: Optional[datetime.datetime] = None
    # The setting name displayed in the user interface.
    display_name: Optional[str] = None
    # The last date and time the setting was modified. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Indicates whether the local admin option is enabled. Default value is false. To enable the local admin option, change the setting to true. If the local admin option is enabled, the end user can be an admin of the Cloud PC device.
    local_admin_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether an end user is allowed to reset their Cloud PC. When true, the user is allowed to reset their Cloud PC. When false, end-user initiated reset is not allowed. The default value is false.
    reset_enabled: Optional[bool] = None
    # Defines how frequently a restore point is created that is, a snapshot is taken) for users' provisioned Cloud PCs (default is 12 hours), and whether the user is allowed to restore their own Cloud PCs to a backup made at a specific point in time.
    restore_point_setting: Optional[CloudPcRestorePointSetting] = None
    # Indicates whether the self-service option is enabled. Default value is false. To enable the self-service option, change the setting to true. If the self-service option is enabled, the end user is allowed to perform some self-service operations, such as upgrading the Cloud PC through the end user portal.
    self_service_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcUserSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .entity import Entity

        from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(CloudPcUserSettingAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localAdminEnabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "resetEnabled": lambda n : setattr(self, 'reset_enabled', n.get_bool_value()),
            "restorePointSetting": lambda n : setattr(self, 'restore_point_setting', n.get_object_value(CloudPcRestorePointSetting)),
            "selfServiceEnabled": lambda n : setattr(self, 'self_service_enabled', n.get_bool_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_bool_value("resetEnabled", self.reset_enabled)
        writer.write_object_value("restorePointSetting", self.restore_point_setting)
        writer.write_bool_value("selfServiceEnabled", self.self_service_enabled)
    


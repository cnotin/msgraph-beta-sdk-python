from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, group, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule_instance

from . import privileged_access_schedule_instance

class PrivilegedAccessGroupEligibilityScheduleInstance(privileged_access_schedule_instance.PrivilegedAccessScheduleInstance):
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedAccessGroupEligibilityScheduleInstance and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance"
        # The identifier of the membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member.
        self._access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
        # The identifier of the privilegedAccessGroupEligibilitySchedule from which this instance was created. Required.
        self._eligibility_schedule_id: Optional[str] = None
        # References the group that is the scope of the membership or ownership eligibility through PIM for groups. Supports $expand.
        self._group: Optional[group.Group] = None
        # The identifier of the group representing the scope of the membership or ownership eligibility through PIM for groups. Required.
        self._group_id: Optional[str] = None
        # Indicates whether the assignment is derived from a group assignment. It can further imply whether the calling principal can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue.
        self._member_type: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType] = None
        # References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand.
        self._principal: Optional[directory_object.DirectoryObject] = None
        # The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for groups. Required.
        self._principal_id: Optional[str] = None
    
    @property
    def access_id(self,) -> Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]:
        """
        Gets the accessId property value. The identifier of the membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member.
        Returns: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]
        """
        return self._access_id
    
    @access_id.setter
    def access_id(self,value: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None) -> None:
        """
        Sets the accessId property value. The identifier of the membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member.
        Args:
            value: Value to set for the access_id property.
        """
        self._access_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupEligibilityScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupEligibilityScheduleInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroupEligibilityScheduleInstance()
    
    @property
    def eligibility_schedule_id(self,) -> Optional[str]:
        """
        Gets the eligibilityScheduleId property value. The identifier of the privilegedAccessGroupEligibilitySchedule from which this instance was created. Required.
        Returns: Optional[str]
        """
        return self._eligibility_schedule_id
    
    @eligibility_schedule_id.setter
    def eligibility_schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the eligibilityScheduleId property value. The identifier of the privilegedAccessGroupEligibilitySchedule from which this instance was created. Required.
        Args:
            value: Value to set for the eligibility_schedule_id property.
        """
        self._eligibility_schedule_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, group, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule_instance

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(privileged_access_group_relationships.PrivilegedAccessGroupRelationships)),
            "eligibilityScheduleId": lambda n : setattr(self, 'eligibility_schedule_id', n.get_str_value()),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_enum_value(privileged_access_group_member_type.PrivilegedAccessGroupMemberType)),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[group.Group]:
        """
        Gets the group property value. References the group that is the scope of the membership or ownership eligibility through PIM for groups. Supports $expand.
        Returns: Optional[group.Group]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the group property value. References the group that is the scope of the membership or ownership eligibility through PIM for groups. Supports $expand.
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The identifier of the group representing the scope of the membership or ownership eligibility through PIM for groups. Required.
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The identifier of the group representing the scope of the membership or ownership eligibility through PIM for groups. Required.
        Args:
            value: Value to set for the group_id property.
        """
        self._group_id = value
    
    @property
    def member_type(self,) -> Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType]:
        """
        Gets the memberType property value. Indicates whether the assignment is derived from a group assignment. It can further imply whether the calling principal can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue.
        Returns: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType]
        """
        return self._member_type
    
    @member_type.setter
    def member_type(self,value: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType] = None) -> None:
        """
        Sets the memberType property value. Indicates whether the assignment is derived from a group assignment. It can further imply whether the calling principal can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue.
        Args:
            value: Value to set for the member_type property.
        """
        self._member_type = value
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand.
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for groups. Required.
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for groups. Required.
        Args:
            value: Value to set for the principal_id property.
        """
        self._principal_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("accessId", self.access_id)
        writer.write_str_value("eligibilityScheduleId", self.eligibility_schedule_id)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
    


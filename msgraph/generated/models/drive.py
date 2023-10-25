from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .drive_item import DriveItem
    from .identity_set import IdentitySet
    from .item_activity_o_l_d import ItemActivityOLD
    from .list_ import List_
    from .quota import Quota
    from .sharepoint_ids import SharepointIds
    from .system_facet import SystemFacet

from .base_item import BaseItem

@dataclass
class Drive(BaseItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.drive"
    # The list of recent activities that took place under this drive.
    activities: Optional[List[ItemActivityOLD]] = None
    # Collection of [bundles][bundle] (albums and multi-select-shared sets of items). Only in personal OneDrive.
    bundles: Optional[List[DriveItem]] = None
    # Describes the type of drive represented by this resource. OneDrive personal drives return personal. OneDrive for Business returns business. SharePoint document libraries return documentLibrary. Read-only.
    drive_type: Optional[str] = None
    # The list of items the user is following. Only in OneDrive for Business.
    following: Optional[List[DriveItem]] = None
    # All items contained in the drive. Read-only. Nullable.
    items: Optional[List[DriveItem]] = None
    # For drives in SharePoint, the underlying document library list. Read-only. Nullable.
    list_: Optional[List_] = None
    # Optional. The user account that owns the drive. Read-only.
    owner: Optional[IdentitySet] = None
    # Optional. Information about the drive's storage space quota. Read-only.
    quota: Optional[Quota] = None
    # The root folder of the drive. Read-only.
    root: Optional[DriveItem] = None
    # The sharePointIds property
    share_point_ids: Optional[SharepointIds] = None
    # Collection of common folders available in OneDrive. Read-only. Nullable.
    special: Optional[List[DriveItem]] = None
    # If present, indicates that this is a system-managed drive. Read-only.
    system: Optional[SystemFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Drive:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Drive
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Drive()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .drive_item import DriveItem
        from .identity_set import IdentitySet
        from .item_activity_o_l_d import ItemActivityOLD
        from .list_ import List_
        from .quota import Quota
        from .sharepoint_ids import SharepointIds
        from .system_facet import SystemFacet

        from .base_item import BaseItem
        from .drive_item import DriveItem
        from .identity_set import IdentitySet
        from .item_activity_o_l_d import ItemActivityOLD
        from .list_ import List_
        from .quota import Quota
        from .sharepoint_ids import SharepointIds
        from .system_facet import SystemFacet

        fields: Dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(ItemActivityOLD)),
            "bundles": lambda n : setattr(self, 'bundles', n.get_collection_of_object_values(DriveItem)),
            "driveType": lambda n : setattr(self, 'drive_type', n.get_str_value()),
            "following": lambda n : setattr(self, 'following', n.get_collection_of_object_values(DriveItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(DriveItem)),
            "list": lambda n : setattr(self, 'list_', n.get_object_value(List_)),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(IdentitySet)),
            "quota": lambda n : setattr(self, 'quota', n.get_object_value(Quota)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(DriveItem)),
            "sharePointIds": lambda n : setattr(self, 'share_point_ids', n.get_object_value(SharepointIds)),
            "special": lambda n : setattr(self, 'special', n.get_collection_of_object_values(DriveItem)),
            "system": lambda n : setattr(self, 'system', n.get_object_value(SystemFacet)),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_collection_of_object_values("bundles", self.bundles)
        writer.write_str_value("driveType", self.drive_type)
        writer.write_collection_of_object_values("following", self.following)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list_)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("quota", self.quota)
        writer.write_object_value("root", self.root)
        writer.write_object_value("sharePointIds", self.share_point_ids)
        writer.write_collection_of_object_values("special", self.special)
        writer.write_object_value("system", self.system)
    


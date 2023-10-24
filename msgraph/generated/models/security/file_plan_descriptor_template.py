from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .authority_template import AuthorityTemplate
    from .category_template import CategoryTemplate
    from .citation_template import CitationTemplate
    from .department_template import DepartmentTemplate
    from .file_plan_reference_template import FilePlanReferenceTemplate
    from .sub_category_template import SubCategoryTemplate

from ..entity import Entity

@dataclass
class FilePlanDescriptorTemplate(Entity):
    # Represents the user who created the filePlanDescriptorTemplate column.
    created_by: Optional[IdentitySet] = None
    # Represents the date and time in which the filePlanDescriptorTemplate is created.
    created_date_time: Optional[datetime.datetime] = None
    # Unique string that defines a filePlanDescriptorTemplate name.
    display_name: Optional[str] = None
    # The OdataType property
    OdataType: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilePlanDescriptorTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilePlanDescriptorTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.authorityTemplate".casefold():
            from .authority_template import AuthorityTemplate

            return AuthorityTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.categoryTemplate".casefold():
            from .category_template import CategoryTemplate

            return CategoryTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.citationTemplate".casefold():
            from .citation_template import CitationTemplate

            return CitationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.departmentTemplate".casefold():
            from .department_template import DepartmentTemplate

            return DepartmentTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanReferenceTemplate".casefold():
            from .file_plan_reference_template import FilePlanReferenceTemplate

            return FilePlanReferenceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subCategoryTemplate".casefold():
            from .sub_category_template import SubCategoryTemplate

            return SubCategoryTemplate()
        return FilePlanDescriptorTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_reference_template import FilePlanReferenceTemplate
        from .sub_category_template import SubCategoryTemplate

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .authority_template import AuthorityTemplate
        from .category_template import CategoryTemplate
        from .citation_template import CitationTemplate
        from .department_template import DepartmentTemplate
        from .file_plan_reference_template import FilePlanReferenceTemplate
        from .sub_category_template import SubCategoryTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
    


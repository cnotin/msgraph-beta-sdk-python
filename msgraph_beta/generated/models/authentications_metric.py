from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class AuthenticationsMetric(Entity):
    # The appid property
    appid: Optional[str] = None
    # The attemptsCount property
    attempts_count: Optional[int] = None
    # The country property
    country: Optional[str] = None
    # The factDate property
    fact_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The successCount property
    success_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationsMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationsMetric
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationsMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appid": lambda n : setattr(self, 'appid', n.get_str_value()),
            "attemptsCount": lambda n : setattr(self, 'attempts_count', n.get_int_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "successCount": lambda n : setattr(self, 'success_count', n.get_int_value()),
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
        writer.write_str_value("appid", self.appid)
        writer.write_int_value("attemptsCount", self.attempts_count)
        writer.write_str_value("country", self.country)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_str_value("os", self.os)
        writer.write_int_value("successCount", self.success_count)
    


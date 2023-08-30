from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact import Artifact
    from .host import Host
    from .ssl_certificate_entity import SslCertificateEntity

from .artifact import Artifact

@dataclass
class SslCertificate(Artifact):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.sslCertificate"
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The fingerprint property
    fingerprint: Optional[str] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The issueDateTime property
    issue_date_time: Optional[datetime.datetime] = None
    # The issuer property
    issuer: Optional[SslCertificateEntity] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The relatedHosts property
    related_hosts: Optional[List[Host]] = None
    # The serialNumber property
    serial_number: Optional[str] = None
    # The sha1 property
    sha1: Optional[str] = None
    # The subject property
    subject: Optional[SslCertificateEntity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SslCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SslCertificate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SslCertificate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .artifact import Artifact
        from .host import Host
        from .ssl_certificate_entity import SslCertificateEntity

        from .artifact import Artifact
        from .host import Host
        from .ssl_certificate_entity import SslCertificateEntity

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "fingerprint": lambda n : setattr(self, 'fingerprint', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "issueDateTime": lambda n : setattr(self, 'issue_date_time', n.get_datetime_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_object_value(SslCertificateEntity)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "relatedHosts": lambda n : setattr(self, 'related_hosts', n.get_collection_of_object_values(Host)),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "sha1": lambda n : setattr(self, 'sha1', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(SslCertificateEntity)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("fingerprint", self.fingerprint)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("issueDateTime", self.issue_date_time)
        writer.write_object_value("issuer", self.issuer)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("relatedHosts", self.related_hosts)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("sha1", self.sha1)
        writer.write_object_value("subject", self.subject)
    


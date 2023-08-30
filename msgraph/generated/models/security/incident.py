from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert import Alert
    from .alert_classification import AlertClassification
    from .alert_comment import AlertComment
    from .alert_determination import AlertDetermination
    from .alert_severity import AlertSeverity
    from .incident_status import IncidentStatus
    from .recommended_hunting_query import RecommendedHuntingQuery

from ..entity import Entity

@dataclass
class Incident(Entity):
    # The list of related alerts. Supports $expand.
    alerts: Optional[List[Alert]] = None
    # Owner of the incident, or null if no owner is assigned. Free editable text.
    assigned_to: Optional[str] = None
    # The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
    classification: Optional[AlertClassification] = None
    # Array of comments created by the Security Operations (SecOps) team when the incident is managed.
    comments: Optional[List[AlertComment]] = None
    # Time when the incident was first created.
    created_date_time: Optional[datetime.datetime] = None
    # Array of custom tags associated with an incident.
    custom_tags: Optional[List[str]] = None
    # The description property
    description: Optional[str] = None
    # Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
    determination: Optional[AlertDetermination] = None
    # The incident name.
    display_name: Optional[str] = None
    # The URL for the incident page in the Microsoft 365 Defender portal.
    incident_web_url: Optional[str] = None
    # The lastModifiedBy property
    last_modified_by: Optional[str] = None
    # Time when the incident was last updated.
    last_update_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommendedActions property
    recommended_actions: Optional[str] = None
    # The recommendedHuntingQueries property
    recommended_hunting_queries: Optional[List[RecommendedHuntingQuery]] = None
    # Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
    redirect_incident_id: Optional[str] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # The status property
    status: Optional[IncidentStatus] = None
    # The systemTags property
    system_tags: Optional[List[str]] = None
    # The Azure Active Directory tenant in which the alert was created.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Incident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Incident
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Incident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert import Alert
        from .alert_classification import AlertClassification
        from .alert_comment import AlertComment
        from .alert_determination import AlertDetermination
        from .alert_severity import AlertSeverity
        from .incident_status import IncidentStatus
        from .recommended_hunting_query import RecommendedHuntingQuery

        from ..entity import Entity
        from .alert import Alert
        from .alert_classification import AlertClassification
        from .alert_comment import AlertComment
        from .alert_determination import AlertDetermination
        from .alert_severity import AlertSeverity
        from .incident_status import IncidentStatus
        from .recommended_hunting_query import RecommendedHuntingQuery

        fields: Dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(Alert)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(AlertClassification)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(AlertComment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customTags": lambda n : setattr(self, 'custom_tags', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(AlertDetermination)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incidentWebUrl": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "recommendedHuntingQueries": lambda n : setattr(self, 'recommended_hunting_queries', n.get_collection_of_object_values(RecommendedHuntingQuery)),
            "redirectIncidentId": lambda n : setattr(self, 'redirect_incident_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(IncidentStatus)),
            "systemTags": lambda n : setattr(self, 'system_tags', n.get_collection_of_primitive_values(str)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_primitive_values("customTags", self.custom_tags)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("determination", self.determination)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_collection_of_object_values("recommendedHuntingQueries", self.recommended_hunting_queries)
        writer.write_str_value("redirectIncidentId", self.redirect_incident_id)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("systemTags", self.system_tags)
        writer.write_str_value("tenantId", self.tenant_id)
    


from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classification_error, classification_job_response, dlp_evaluate_policies_job_response, entity, evaluate_label_job_response

from . import entity

class JobResponseBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new jobResponseBase and sets the default values.
        """
        super().__init__()
        # The creationDateTime property
        self._creation_date_time: Optional[datetime] = None
        # The endDateTime property
        self._end_date_time: Optional[datetime] = None
        # The error property
        self._error: Optional[classification_error.ClassificationError] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The startDateTime property
        self._start_date_time: Optional[datetime] = None
        # The status property
        self._status: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The type property
        self._type: Optional[str] = None
        # The userId property
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> JobResponseBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: JobResponseBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.classificationJobResponse":
                from . import classification_job_response

                return classification_job_response.ClassificationJobResponse()
            if mapping_value == "#microsoft.graph.dlpEvaluatePoliciesJobResponse":
                from . import dlp_evaluate_policies_job_response

                return dlp_evaluate_policies_job_response.DlpEvaluatePoliciesJobResponse()
            if mapping_value == "#microsoft.graph.evaluateLabelJobResponse":
                from . import evaluate_label_job_response

                return evaluate_label_job_response.EvaluateLabelJobResponse()
        return JobResponseBase()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The creationDateTime property
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The creationDateTime property
        Args:
            value: Value to set for the creation_date_time property.
        """
        self._creation_date_time = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    @property
    def error(self,) -> Optional[classification_error.ClassificationError]:
        """
        Gets the error property value. The error property
        Returns: Optional[classification_error.ClassificationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[classification_error.ClassificationError] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classification_error, classification_job_response, dlp_evaluate_policies_job_response, entity, evaluate_label_job_response

        fields: Dict[str, Callable[[Any], None]] = {
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(classification_error.ClassificationError)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    


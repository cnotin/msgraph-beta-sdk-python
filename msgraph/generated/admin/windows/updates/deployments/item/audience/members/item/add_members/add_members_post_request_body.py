from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from ..........models.windows_updates import updatable_asset

class AddMembersPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the addMembers method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def assets(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the assets property value. The assets property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._assets
    
    @assets.setter
    def assets(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the assets property value. The assets property
        Args:
            value: Value to set for the assets property.
        """
        self._assets = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new addMembersPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assets property
        self._assets: Optional[List[updatable_asset.UpdatableAsset]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddMembersPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddMembersPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddMembersPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assets": lambda n : setattr(self, 'assets', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("assets", self.assets)
        writer.write_additional_data_value(self.additional_data)
    


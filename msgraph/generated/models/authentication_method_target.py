from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_target_type import AuthenticationMethodTargetType
    from .entity import Entity
    from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
    from .sms_authentication_method_target import SmsAuthenticationMethodTarget
    from .voice_authentication_method_target import VoiceAuthenticationMethodTarget

from .entity import Entity

@dataclass
class AuthenticationMethodTarget(Entity):
    # Determines if the user is enforced to register the authentication method.
    is_registration_required: Optional[bool] = None
    # The OdataType property
    OdataType: Optional[str] = None
    # The targetType property
    target_type: Optional[AuthenticationMethodTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget".casefold():
            from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget

            return MicrosoftAuthenticatorAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodTarget".casefold():
            from .sms_authentication_method_target import SmsAuthenticationMethodTarget

            return SmsAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodTarget".casefold():
            from .voice_authentication_method_target import VoiceAuthenticationMethodTarget

            return VoiceAuthenticationMethodTarget()
        return AuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target_type import AuthenticationMethodTargetType
        from .entity import Entity
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget
        from .voice_authentication_method_target import VoiceAuthenticationMethodTarget

        from .authentication_method_target_type import AuthenticationMethodTargetType
        from .entity import Entity
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget
        from .voice_authentication_method_target import VoiceAuthenticationMethodTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "isRegistrationRequired": lambda n : setattr(self, 'is_registration_required', n.get_bool_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(AuthenticationMethodTargetType)),
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
        writer.write_bool_value("isRegistrationRequired", self.is_registration_required)
        writer.write_enum_value("targetType", self.target_type)
    


from enum import Enum

class ConditionalAccessGuestOrExternalUserTypes(Enum):
    None_escaped = "none",
    InternalGuest = "internalGuest",
    B2bCollaborationGuest = "b2bCollaborationGuest",
    B2bCollaborationMember = "b2bCollaborationMember",
    B2bDirectConnectUser = "b2bDirectConnectUser",
    OtherExternalUser = "otherExternalUser",
    ServiceProvider = "serviceProvider",
    UnknownFutureValue = "unknownFutureValue",


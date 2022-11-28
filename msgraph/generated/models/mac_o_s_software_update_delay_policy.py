from enum import Enum

class MacOSSoftwareUpdateDelayPolicy(Enum):
    # Software update delays will not be enforced.
    None_escaped = "none",
    # Force delays for OS software updates.
    DelayOSUpdateVisibility = "delayOSUpdateVisibility",
    # Force delays for app software updates.
    DelayAppUpdateVisibility = "delayAppUpdateVisibility",
    # Sentinel member for cases where the client cannot handle the new enum values.
    UnknownFutureValue = "unknownFutureValue",
    # Force delays for major OS software updates.
    DelayMajorOsUpdateVisibility = "delayMajorOsUpdateVisibility",


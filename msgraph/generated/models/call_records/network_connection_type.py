from enum import Enum

class NetworkConnectionType(Enum):
    Unknown = "unknown",
    Wired = "wired",
    Wifi = "wifi",
    Mobile = "mobile",
    Tunnel = "tunnel",
    UnknownFutureValue = "unknownFutureValue",


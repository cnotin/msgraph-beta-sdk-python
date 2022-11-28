from enum import Enum

class SecureBootWithDMAType(Enum):
    # Not configured, no operation
    NotConfigured = "notConfigured",
    # Turns on VBS with Secure Boot
    WithoutDMA = "withoutDMA",
    # Turns on VBS with Secure Boot and DMA
    WithDMA = "withDMA",


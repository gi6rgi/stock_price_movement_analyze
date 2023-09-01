from enum import Enum


class EMACalculationType(str, Enum):
    OPEN = "open"
    CLOSE = "close"
    HIGH = "high"
    LOW = "low"

from enum import Enum

class RideStatus(Enum):
    REQUESTED = "requested"
    ASSIGNED = "assigned"
    STARTED = "started"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
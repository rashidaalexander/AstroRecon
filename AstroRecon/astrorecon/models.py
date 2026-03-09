
from dataclasses import dataclass

@dataclass
class Summary:
    project: str
    status: str
    notes: str = "Open-source orbital infrastructure reconnaissance engine"

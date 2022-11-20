from dataclasses import dataclass
from datetime import timedelta

@dataclass 
class ConfigItem():
    delta : timedelta
    entities : list
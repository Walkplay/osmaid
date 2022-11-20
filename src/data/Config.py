from dataclasses import dataclass
from data.ConfigItem import ConfigItem

@dataclass 
class Config():
    items : list[ConfigItem]
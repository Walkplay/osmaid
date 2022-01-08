from dataclasses import dataclass

@dataclass 
class Config():
    session : list
    daily : list
    weekly : list
    monthly : list
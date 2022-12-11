from enum import Enum

class IType(Enum):
    IMG: int = 0
    BG: int = 1
    STR: list = ["img", "bg"]

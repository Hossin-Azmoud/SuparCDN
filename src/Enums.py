from enum import Enum
from dataclasses import dataclass

class IType(Enum):
    IMG: int = 0
    BG: int = 1
    NAMES: list = ["img", "bg"]

@dataclass
class Response:
    code: int
    data: any

    def __dict__(self) -> dict:
        return {
            "code": self.code,
            "data": self.data
        }

def makeResponse(code: int = 200, data: any = "No data") -> None: return dict(Response(code, data))

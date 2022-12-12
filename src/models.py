from dataclasses import dataclass

@dataclass
class Response:
    code: int
    data: any

    def __dict__(self) -> dict:
        return {
            "code": self.code,
            "data": self.data
        }

from typing import Optional

from pydantic import BaseModel


class MathsResponse(BaseModel):
    status_code: int = 200
    message: str
    data: Optional[int]

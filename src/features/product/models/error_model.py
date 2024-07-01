from pydantic import BaseModel


class ErrorModel(BaseModel):
    """Model used for Error response"""

    message: str

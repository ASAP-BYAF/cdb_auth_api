from pydantic import BaseModel


class AuthBase(BaseModel):
    password: str


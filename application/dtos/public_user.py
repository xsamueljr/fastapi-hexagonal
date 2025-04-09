from pydantic import BaseModel


class PublicUser(BaseModel):
    id: str
    name: str

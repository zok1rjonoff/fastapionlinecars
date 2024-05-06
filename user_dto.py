from pydantic import *


class UserDto(BaseModel):
    name: str
    phone_number: str
    password: str




from pydantic import BaseModel, EmailStr, Field, ConfigDict


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True

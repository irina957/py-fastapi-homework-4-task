from datetime import date
from pydantic import BaseModel, field_validator, ConfigDict, HttpUrl
from validation import validate_name, validate_gender, validate_birth_date


class ProfileResponseSchema(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str
    avatar: HttpUrl

    model_config = ConfigDict(from_attributes=True)


class ProfileCreateSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str

    @field_validator("first_name", "last_name")
    @classmethod
    def check_names(cls, v: str) -> str:
        validate_name(v)
        return v.lower().strip()

    @field_validator("gender")
    @classmethod
    def check_gender(cls, v: str) -> str:
        validate_gender(v)
        return v

    @field_validator("date_of_birth")
    @classmethod
    def check_birth_date(cls, v: date) -> date:
        validate_birth_date(v)
        return v

    @field_validator("info")
    @classmethod
    def check_info(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("Info cannot be empty or consist only of spaces.")
        return v

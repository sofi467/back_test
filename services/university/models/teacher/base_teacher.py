from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class DegreeEnum(StrEnum):
    MATHEMATICS = "Mathematics"
    PHYSICS = "Physics"
    HISTORY = "History"
    GEOGRAPHY = "Geography"


class BaseTeacher(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    subject: DegreeEnum

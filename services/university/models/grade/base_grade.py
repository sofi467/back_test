from pydantic import BaseModel, ConfigDict, Field
from services.constans import GRADE_MAX, GRADE_MIN


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=GRADE_MIN, le=GRADE_MAX)

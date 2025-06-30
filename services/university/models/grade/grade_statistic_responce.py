from pydantic import BaseModel, ConfigDict, Field


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0)
    min: int | None
    max: int | None
    avg: int | None

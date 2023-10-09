from pydantic import BaseModel, validator

class Post(BaseModel):
    id: int
    title: str

    @validator('id')
    def check_id_less_then_two(cls, n):
        if n > 2:
            raise ValueError('Id not less than two')
        else:
            return n


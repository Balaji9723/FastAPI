from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str
    # description: str | None=None
    # completed : bool= False

# class TodoCreate(BaseModel):
#     pass

class TodoSchema(BaseModel):
    id: int
    title: str
    description: str

class Config:
    from_attributes = True

# class Todo(TodoBase):
#     id: int
#     class config:
#         orm_mode = True
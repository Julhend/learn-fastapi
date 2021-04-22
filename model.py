from pydantic import BaseModel, Field

# Models


class UserList(BaseModel):
    id: str
    username: str
    password: str
    first_name: str
    last_name: str
    gender: str
    create_at: str
    status: str


class UserEntry(BaseModel):
    username: str = Field(..., example="Julhen")
    password: str = Field(..., example="test")
    first_name: str = Field(..., example="jul")
    last_name: str = Field(..., example="hen")
    gender: str = Field(..., example="M")


class UserUpdate(BaseModel):
    id: str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="jul")
    last_name: str = Field(..., example="hen")
    gender: str = Field(..., example="M")
    status: str = Field(..., example="1")


class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")

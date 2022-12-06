import pydantic as _pydantic


class _BaseUser(_pydantic.BaseModel):
    name: str
    surname: str
    thirdname: str
    phone: str
    review: str


class User(_BaseUser):
    id: int

    class Config:
        orm_mode = True


class CreateUser(_BaseUser):
    pass

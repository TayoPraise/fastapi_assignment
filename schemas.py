import datetime as _dt
import pydantic as _pydantic

class _BaseCompany(_pydantic.BaseModel):
    company_name: str
    country: str
    email: str
    valuation: int

class Company(_BaseCompany):
    id: int
    date_created: _dt.datetime

    class Config:
        # orm_mode = True
        from_attributes = True


class CreateCompany(_BaseCompany):
    pass
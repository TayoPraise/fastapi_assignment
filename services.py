from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas
import sqlalchemy.orm as _orm

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def add_tables():
    # this function add tables to the database we are connected to
    return _database.Base.metadata.create_all(bind = _database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_company( company: _schemas.CreateCompany, db: "Session") -> _schemas.Company:
    company  = _models.Company(**company.dict())
    db.add(company)
    db.commit()
    db.refresh(company)
    return _schemas.Company.model_validate(company)

async def get_all_companies(db: "Session") -> List[_schemas.Company]:
    company = db.query(_models.Company).all()
    return list(map(_schemas.Company.model_validate, company))

async def get_company(company_id: int, db: "Session"):
    company = db.query(_models.Company).filter(_models.Company.id == company_id).first()
    return company

async def delete_company(company: _models.Company, db: "Session"):
    db.delete(company)
    db.commit()

async def update_company(company_data: _schemas.CreateCompany, company: _models.Company, db: "Session") -> _schemas.Company:
    company.company_name = company_data.company_name
    company.country = company_data.country
    company.email = company_data.email
    company.valuation = company_data.valuation

    db.commit()
    db.refresh(company)

    return _schemas.Company.model_validate(company)
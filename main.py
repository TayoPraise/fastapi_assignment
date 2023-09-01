from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

@app.post("/api/companies/", response_model = _schemas.Company)
async def create_company(company: _schemas.CreateCompany, db: _orm.Session = _fastapi.Depends(_services.get_db), ):
    return await _services.create_company(company=company, db=db)

@app.get("/api/companies/", response_model=List[_schemas.Company])
async def get_company(db:_orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_companies(db=db)

@app.get("/api/companies/{company_id}/", response_model = _schemas.Company)
async def get_company(company_id: int, db:_orm.Session = _fastapi.Depends(_services.get_db)):

    company = await _services.get_company(db=db, company_id=company_id)
    if company is None:
        raise _fastapi.HTTPException(status_code=404, detail = "Company details with id does not exist")
    
    return company

@app.delete("/api/companies/{company_id}/")
async def delete_company(company_id: int, db:_orm.Session = _fastapi.Depends(_services.get_db)):
    company = await _services.get_company(db = db, company_id = company_id)
    if company is None:
        raise _fastapi.HTTPException(status_code=404, detail = "Company details with id does not exist")
    
    await _services.delete_company(company, db=db)
    return "Successfully deleted this company"

@app.put("/api/companies/{company_id}/", response_model=_schemas.Company)
async def update_company(company_id: int, contact_data: _schemas.CreateCompany, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    company = await _services.get_company(db=db, company_id=company_id)
    if company is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact with id does not exist")

    return await _services.update_company(company_data=company_data, company=company, db=db)
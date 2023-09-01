import datetime as _dt
import sqlalchemy as _sql

import database as _database

class Company(_database.Base):
    __tablename__ = "companies"
    id = _sql.Column(_sql.Integer, primary_key = True, index= True)
    company_name = _sql.Column(_sql.String, index= True)
    country = _sql.Column(_sql.String, index= True)
    email = _sql.Column(_sql.String, index= True, unique = True)
    valuation = _sql.Column(_sql.Integer, index= True)
    date_created = _sql.Column(_sql.DateTime, default = _dt.datetime.utcnow)
    
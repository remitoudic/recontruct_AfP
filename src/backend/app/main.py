from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db

# Create the database tables if they don't exist
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AfP Pawnshop API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AfP Pawnshop API"}

@app.get("/api/customers", response_model=List[schemas.Customer])
def get_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = db.query(models.Customer).offset(skip).limit(limit).all()
    return customers

@app.post("/api/customers", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/api/pawns", response_model=List[schemas.Pawn])
def get_pawns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pawns = db.query(models.Pawn).offset(skip).limit(limit).all()
    return pawns

@app.get("/api/ledger", response_model=List[schemas.Ledger])
def get_ledger(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = db.query(models.Ledger).offset(skip).limit(limit).all()
    return entries

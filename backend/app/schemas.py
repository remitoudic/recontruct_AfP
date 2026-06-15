from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

# CUSTOMERS
class CustomerBase(BaseModel):
    name: str
    vorname: str
    geburtstag: Optional[date] = None
    geburtsort: Optional[str] = None
    wohnort: Optional[str] = None
    strasse: Optional[str] = None
    personr: Optional[str] = None
    legitimation: Optional[str] = None
    behoerde: Optional[str] = None
    erstervertrag: Optional[int] = None
    sperre: bool = False

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

# PAWNS
class PawnBase(BaseModel):
    datum: date
    betrag: float
    unkosten: float
    status: int = 0
    enddatum: Optional[date] = None
    vorgaenger_id: Optional[int] = None
    nachfolger_id: Optional[int] = None
    next: Optional[int] = None
    versart: int = 0
    gegenstand: str
    lager: Optional[str] = None

class PawnCreate(PawnBase):
    kunde_id: int

class Pawn(PawnBase):
    id: int
    kunde_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

# LEDGER
class LedgerBase(BaseModel):
    datum: date
    betrag: float
    posten: str
    konto: Optional[int] = None
    status: int = 0
    pawn_id: Optional[int] = None

class LedgerCreate(LedgerBase):
    pass

class Ledger(LedgerBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

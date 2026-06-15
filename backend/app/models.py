from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    vorname = Column(String(255), nullable=False)
    geburtstag = Column(Date)
    geburtsort = Column(String(255))
    wohnort = Column(String(255))
    strasse = Column(String(255))
    personr = Column(String(100))
    legitimation = Column(String(100))
    behoerde = Column(String(100))
    erstervertrag = Column(Integer)
    sperre = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    pawns = relationship("Pawn", back_populates="customer")


class Pawn(Base):
    __tablename__ = "pawns"

    id = Column(Integer, primary_key=True, index=True)
    kunde_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    datum = Column(Date, nullable=False)
    betrag = Column(Numeric(12, 2), nullable=False)
    unkosten = Column(Numeric(12, 2), nullable=False)
    status = Column(Integer, default=0, nullable=False)
    enddatum = Column(Date)
    vorgaenger_id = Column(Integer, ForeignKey("pawns.id", ondelete="SET NULL"))
    nachfolger_id = Column(Integer, ForeignKey("pawns.id", ondelete="SET NULL"))
    next = Column(Integer)
    versart = Column(Integer, default=0, nullable=False)
    gegenstand = Column(Text, nullable=False)
    lager = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    customer = relationship("Customer", back_populates="pawns")
    transactions = relationship("Ledger", back_populates="pawn")


class Ledger(Base):
    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True, index=True)
    datum = Column(Date, nullable=False)
    betrag = Column(Numeric(12, 2), nullable=False)
    posten = Column(String(255), nullable=False)
    konto = Column(Integer)
    status = Column(Integer, default=0, nullable=False)
    pawn_id = Column(Integer, ForeignKey("pawns.id", ondelete="SET NULL"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    pawn = relationship("Pawn", back_populates="transactions")

-- Initial schema for modern AfP Pawnshop Web App

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    vorname VARCHAR(255) NOT NULL,
    geburtstag DATE,
    geburtsort VARCHAR(255),
    wohnort VARCHAR(255),
    strasse VARCHAR(255),
    personr VARCHAR(100),
    legitimation VARCHAR(100),
    behoerde VARCHAR(100),
    erstervertrag INTEGER,
    sperre BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pawns (
    id SERIAL PRIMARY KEY,
    kunde_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    datum DATE NOT NULL,
    betrag DECIMAL(12,2) NOT NULL,
    unkosten DECIMAL(12,2) NOT NULL,
    status INTEGER NOT NULL DEFAULT 0,
    enddatum DATE,
    vorgaenger_id INTEGER REFERENCES pawns(id) ON DELETE SET NULL,
    nachfolger_id INTEGER REFERENCES pawns(id) ON DELETE SET NULL,
    next INTEGER,
    versart INTEGER NOT NULL DEFAULT 0,
    gegenstand TEXT NOT NULL,
    lager VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ledger (
    id SERIAL PRIMARY KEY,
    datum DATE NOT NULL,
    betrag DECIMAL(12,2) NOT NULL,
    posten VARCHAR(255) NOT NULL,
    konto INTEGER,
    status INTEGER NOT NULL DEFAULT 0,
    pawn_id INTEGER REFERENCES pawns(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

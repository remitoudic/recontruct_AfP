# Database Schema Diagram

Below is the Entity-Relationship (ER) diagram for the AfP Pawnshop application, illustrating the three core tables and their relationships.

```mermaid
erDiagram
    kunden {
        int id PK
        varchar name
        varchar vorname
        date geburtstag
        varchar geburtsort
        varchar wohnort
        varchar strasse
        varchar personr
        varchar legitimation
        varchar behoerde "behörde"
        int erstervertrag
        tinyint sperre
    }

    pfand {
        int id PK
        int kunde FK "References kunden(id)"
        date datum
        decimal betrag
        decimal unkosten
        int Status
        date enddatum
        int vorgaenger "vorgänger"
        int nachfolger
        int next
        int versart
        text gegenstand
        varchar lager
        decimal dmbetrag
        decimal dmunkosten
    }

    einaus {
        int id PK
        date datum
        decimal betrag
        varchar posten
        decimal dmbetrag
        int konto
        int status
        int pfand FK "References pfand(id)"
    }

    %% Relationships
    kunden ||--o{ pfand : "owns / pawns"
    pfand ||--o{ einaus : "has transactions (ledger)"
    
    %% Self-referential relationship for renewing a pawn ticket
    pfand ||--o| pfand : "vorgänger / nachfolger (renewals)"
```

### Explanation of Relationships:
- **`kunden` to `pfand` (One-to-Many):** One customer (`kunden`) can pawn multiple items or have multiple pawn tickets (`pfand`). The `kunde` column in the `pfand` table acts as the foreign key.
- **`pfand` to `einaus` (One-to-Many):** A specific pawn ticket (`pfand`) can have multiple cashbook ledger entries (`einaus`) - for example, the initial payout, fee payments, or final redemption. The `pfand` column in `einaus` links the transaction to the item.
- **`pfand` to `pfand` (One-to-One):** When a pawn ticket is extended (renewed), the legacy system points the old ticket to a new ticket using the `vorgänger` (predecessor) and `nachfolger` (successor) integer fields.

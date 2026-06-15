# Features & Extracted Business Logic

This document summarizes the core functionalities of the legacy **AfP** (Anwendung für Pfandhäuser) software based on strings and schemas extracted from the binary files.

## 1. Customer Management (Kundenverwaltung)
*   **Customer Profiles:** The app stores customers with fields for Name, First Name, Date of Birth, Place of Birth, Address (Street, City).
*   **Identity Verification:** It mandates ID tracking via `personr` (ID Card Number), `legitimation` (ID type), and `behörde` (Issuing Authority).
*   **Customer Locking:** The `sperre` boolean field indicates a customer can be blacklisted or barred from pawning new items.

## 2. Pawn Management (Pfandverwaltung)
*   **Pawn Tickets:** An item (`gegenstand`) is pawned by a customer (`kunde`). The ticket includes the loan amount (`betrag`), the incurred fees (`unkosten`), and the due date (`enddatum`).
*   **Storage Tracking:** The `lager` field tracks the physical storage location of the pawned item inside the shop.
*   **Renewals & Extensions:** The system uses a linked-list mechanism. A pawn ticket can have a `vorgänger` (predecessor) and a `nachfolger` (successor). When a customer extends the pawn ticket instead of redeeming it, a new ticket is generated and linked to the old one.

## 3. Financials & Cashbook (Kassenbuch)
*   **Ledger (Einnahmen/Ausgaben):** Every transaction (pawning an item, redeeming, paying fees) is logged in the `einaus` table.
*   **References:** Ledger entries reference the specific pawn ticket (`pfand`).
*   **Historical Legacy:** The software originally managed the Deutsche Mark (DM) to Euro conversion around 2002, converting `dmbetrag` to `betrag` using the official `1.95583` exchange rate.

## 4. UI Capabilities (Derived from Strings)
*   **List Printing (Listendruck):** Likely used for generating reports on inventory, due items, or daily cashbook balances.
*   **Ticket Printing (Pfandscheindruck):** Generating the physical ticket given to the customer.
*   **Cashbook Reconciliation:** A function `Kassenbuch vervollständigen` ensures all transactions are accounted for properly.

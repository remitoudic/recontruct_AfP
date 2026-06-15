# AfP Pawnshop Application - User Documentation

Welcome to the AfP Pawnshop Application User Guide. This software is designed to streamline your daily shop operations, from registering customers and issuing pawn tickets to balancing your cash drawer at the end of the day.

---

## 1. Dashboard & Overview
When you log into the application, you are greeted by the **Dashboard**. 
Here, you will see:
*   **Daily Summary:** Total cash in/out for the day.
*   **Expiring Pawns:** Alerts for pawn tickets that are due or expiring soon, allowing you to follow up or process defaults.

---

## 2. Customer Management (Kunden)
Before you can issue a pawn ticket, the individual must be registered in the system.

### Adding a New Customer
1. Navigate to the **Customers** tab.
2. Click **Add Customer**.
3. Fill in their details: First Name, Last Name, Date of Birth, and Address.
4. **Mandatory ID Verification:** You must log their ID Card Number (`personr`), the type of ID (`legitimation`), and the issuing authority (`behörde`).

### Blocking a Customer
If a customer is no longer allowed to pawn items (e.g., due to previous defaults or fraud), you can set their profile to **Blocked** (`sperre`). The system will prevent any new tickets from being issued to a blocked customer.

---

## 3. Pawn Ticketing (Pfand)
This module handles receiving items and issuing cash loans.

### Issuing a New Ticket
1. Select a registered customer and click **New Pawn Ticket**.
2. **Item Details:** Enter a clear description of the item (`gegenstand`).
3. **Storage:** Note exactly where the item is stored in the back room (`lager`) so it can be easily found later.
4. **Financials:** Enter the loan amount paid to the customer (`betrag`) and any initial setup fees (`unkosten`).
5. **Print:** The system will generate a PDF pawn ticket. Print it and give it to the customer.

### Renewing or Extending a Ticket
If the due date (`enddatum`) arrives and the customer wishes to extend the loan rather than redeem the item:
1. Locate the active pawn ticket.
2. Click **Extend/Renew**.
3. The customer must pay the accrued interest and fees. Once paid, the system automatically marks the old ticket as complete and generates a **new ticket** linked to the old one.

### Redeeming an Item
When a customer returns to pay back their loan:
1. Locate the ticket.
2. Click **Redeem**.
3. Collect the original loan amount plus all accumulated fees. The system will mark the ticket as closed and update the cashbook.

---

## 4. The Cashbook (Kassenbuch)
The Cashbook (or Ledger) is the financial heart of the pawnshop. It ensures every cent is tracked.

### Automatic Entries
You rarely need to enter things manually. The system automatically creates ledger entries when:
*   Cash is given out for a new pawn ticket.
*   Cash comes in from a ticket renewal (fees collected).
*   Cash comes in from a ticket redemption (loan repayment + fees).

### Daily Reconciliation
At the end of the day, navigate to the **Ledger** tab.
*   Compare the **System Total** to the physical cash in your drawer.
*   If you need to add manual adjustments (e.g., paying a cleaner from the register, or depositing money to the bank), you can click **Add Manual Entry** and specify the amount and reason (`posten`).

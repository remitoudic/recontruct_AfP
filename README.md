# AfP (Anwendung für Pfandhäuser) - Modern Web App

Welcome to the modernized version of the AfP Pawnshop software! This application is a complete reconstruction of a legacy Delphi/MySQL 5.0 desktop app, rebuilt as a cloud-native, containerized web application

---

## 🏗 System Architecture

This application is built using a modern full-stack architecture orchestrated by Docker Compose. It consists of three main services:

1.  **Database (`db`):** PostgreSQL 15.
2.  **Backend (`backend`):** A high-performance Python REST API built with **FastAPI** and **SQLAlchemy**.
3.  **Frontend (`frontend`):** A fast, reactive single-page application built with **SvelteKit**.

---

## 🚀 How to Run the Software (Local Development)

### Prerequisites
You must have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.

### Starting the Application
1. Open your terminal and navigate to the root directory of this project.
2. Run the following command to build and start all services in the background:
   ```bash
   docker-compose up --build -d
   ```
3. Docker will download the necessary images, install Python and Node.js dependencies, and initialize the PostgreSQL database.

### Accessing the Services
Once the containers are running, you can access the different parts of the application via your web browser:

*   🖥 **Frontend (SvelteKit UI):** [http://localhost:3000](http://localhost:3000)
    *   *This is the main user interface where clerks will interact with the system.*
*   ⚙️ **Backend API (FastAPI):** [http://localhost:8000](http://localhost:8000)
*   📚 **Interactive API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
    *   *Use the Swagger UI here to test API endpoints (like creating a customer or issuing a pawn ticket) directly from your browser.*

### Stopping the Application
To stop the application and shut down the containers, run:
```bash
docker-compose down
```

---

## 💼 Core Business Features (How to Use the App)

The software is designed to manage the day-to-day operations of a pawnshop. Here are the core modules:

### 1. Customer Management (Kunden)
Before a pawn ticket can be issued, the customer must be registered.
*   **What it tracks:** Name, birthdate, address, and ID verification details (ID card number and issuing authority).
*   **Customer Locking (`sperre`):** You can flag a customer to block them from pawning items in the future.

### 2. Pawn Ticketing (Pfand)
This is the core of the business. 
*   **Issuing a Ticket:** A clerk inputs the item description (`gegenstand`), the physical storage bin/location (`lager`), the loan amount (`betrag`), and any initial fees (`unkosten`).
*   **Renewals & Extensions:** If a customer cannot pay back the loan by the due date (`enddatum`), they can extend the pawn by paying the outstanding interest/fees. The software manages this by linking the old ticket to a brand-new ticket (using the `vorgaenger` and `nachfolger` tracking).

### 3. The Cashbook Ledger (Kassenbuch / Einaus)
The system maintains a strict, balanced ledger.
*   **Tracking Cashflow:** Every time cash leaves the register (a loan is paid out) or enters the register (a fee is collected, or a loan is repaid), a record is automatically generated in the ledger.
*   **Reconciliation:** Clerks can review the daily ledger to ensure the physical cash in the drawer matches the digital records.

---

## 🛠 Development & Code Structure

If you wish to edit the code:
*   **Database Schema:** Look at `src/db/init.sql`. This file is only executed the *very first time* the database container starts. If you change it later, you must delete the Docker volume to force a reset.
*   **Backend Logic:** Found in `src/backend/app/`. The API endpoints are in `main.py`, database models in `models.py`, and data validation rules in `schemas.py`.
*   **Frontend UI:** Found in `src/frontend/`. This is a standard SvelteKit layout.

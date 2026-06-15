# Rebuilding AfP as a Web Application - High-Level Guide

This document outlines the step-by-step strategy for rebuilding the legacy AfP (Anwendung für Pfandhäuser) Windows desktop software as a modern, cloud-native web application.

## Step 1: Technology Stack Selection
To build a scalable and maintainable web application, we recommend a modern stack:
*   **Database:** PostgreSQL (Robust, relational, highly compatible with the legacy MySQL structure).
*   **Backend:** Node.js (with Express/NestJS), Python (FastAPI/Django), or Go. The backend will serve a RESTful or GraphQL API.
*   **Frontend:** React (Next.js) or Vue (Nuxt.js) with Tailwind CSS. Since this is an internal business tool, a UI component library like Shadcn UI or MUI is highly recommended for building fast, dense data tables and forms.
*   **Hosting:** AWS, Vercel, or a simple VPS with Docker.

## Step 2: Database Design & Modernization
We will map the old 3-table structure to a modern PostgreSQL schema.
*   **Cleanup:** Remove all legacy `dmbetrag` and `dmunkosten` columns (Deutsche Mark references are obsolete).
*   **Normalization:** 
    *   Create a `Customers` table (from `kunden`).
    *   Create a `PawnTickets` table (from `pfand`).
    *   Create a `Transactions` / `Ledger` table (from `einaus`).
*   **Timestamps:** Add `created_at` and `updated_at` columns to all tables for modern auditing.

## Step 3: API & Backend Development
Develop backend services to handle the core business logic:
*   **Authentication & Authorization:** The old app used Windows users. The new app needs a proper login system (e.g., JWT) with Roles (Admin vs. Shop Clerk).
*   **Customer API:** Endpoints to Create, Read, Update, and Block (`sperre`) customers.
*   **Pawn Lifecycle API:**
    *   Endpoint to issue a new pawn ticket.
    *   Endpoint to calculate fees based on time elapsed.
    *   Endpoint to extend/renew a ticket (creating the `successor` record).
    *   Endpoint to redeem a ticket.
*   **Ledger API:** Endpoints to automatically write to the Cashbook (`einaus`) whenever money moves in or out.

## Step 4: Frontend Development
Build the user interface for the shop clerks:
*   **Dashboard:** Shows daily summaries, cashbook balance, and alerts for pawn tickets that are expiring soon.
*   **Customer Management View:** A table to search, add, and edit customers, along with their ID verification details.
*   **Pawn Management View:** Forms to input new pawned items (`gegenstand`), set loans (`betrag`), and assign storage bins (`lager`).
*   **Cashbook View:** A daily ledger view.

## Step 5: Document Generation (Printing)
The old software printed directly to dot-matrix or inkjet printers. 
*   Implement server-side PDF generation (using libraries like Puppeteer, PDFKit, or ReportLab).
*   Create templates for the **Pawn Ticket (Pfandschein)** and **Daily Reports (Listendruck)** so they can be easily printed from any web browser.

## Step 6: Data Migration
*   Write a one-time migration script to extract the data from the legacy MySQL 5.0 database and insert it into the new PostgreSQL database.
*   Map the old `id` fields precisely so the historic links between pawn tickets (`vorgänger`/`nachfolger`) remain intact.

## Step 7: Testing & Deployment
*   Test the business logic rigorously, especially the fee calculation and ledger balancing.
*   Deploy the application securely via HTTPS, ensuring data backups are automated (replacing the old `DirSync` manual backups).

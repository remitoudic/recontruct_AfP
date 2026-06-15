# AfP Modernization Project

## Overview
This repository is dedicated to the modernization and reconstruction of **AfP (Anwendung für Pfandhäuser)** — a legacy Windows desktop pawnshop application originally developed in Delphi and powered by a MySQL 5.0 database. 

The goal of this project is to rebuild the application from the ground up as a modern, scalable, and cloud-native **web application** while preserving the core business logic, customer tracking, and financial ledger features of the original software.

## Repository Structure
Because the original source code was unavailable, the core logic and database schemas were reverse-engineered directly from the legacy Windows executables. 

You will find all the documentation and specifications required to rebuild the application in the `recontruct/` directory:

*   **`recontruct/README.md`**: A high-level, step-by-step technical guide for rebuilding the application using modern web technologies (e.g., PostgreSQL, Node.js/Python, and React/Vue).
*   **`recontruct/features_and_logic.md`**: Detailed breakdown of the extracted business logic, including customer management, pawn ticketing lifecycle, and cashbook accounting.
*   **`recontruct/database_schema.sql`**: The reverse-engineered SQL database schema.
*   **`recontruct/database_diagram.md`**: A visual Entity-Relationship (ER) diagram representing the core data model.

# GreenLogix Source Systems

## Project Overview

GreenLogix is a logistics company that delivers freight across the United States.

The purpose of this project is to build a modern data warehouse in Snowflake by integrating data from multiple operational source systems.

---

## Source Systems

### 1. Warehouse Management System (PostgreSQL)

Purpose:
Manages customer orders and warehouse operations.

Technology:
PostgreSQL (Neon)

Tables:
- customers
- loads
- routes
- facilities

---

### 2. Fleet Management System (CSV Files)

Purpose:
Stores fleet assets and driver information.

Technology:
CSV Files

Files:
- drivers.csv
- trucks.csv
- trailers.csv
- trips.csv
- fuel_purchases.csv
- maintenance_records.csv
- safety_incidents.csv

---

### 3. GPS Provider

Purpose:
Provides live GPS tracking information.

Technology:
REST JSON API

Status:
To be implemented

---

### 4. Sustainability System

Purpose:
Stores environmental reporting information.

Technology:
SQL Server

Status:
To be implemented
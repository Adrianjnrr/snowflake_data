# Snowflake Data Platform

An end-to-end ELT data engineering project built with:

- Snowflake
- Snowpark for Python
- DBT
- PostgreSQL
- Python
- Power BI

## Architecture

CSV / PostgreSQL
        ↓
Python Ingestion
        ↓
Snowflake STAGING
        ↓
Transform
        ↓
Star Schema
        ↓
Power BI
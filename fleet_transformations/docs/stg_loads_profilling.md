# STG_LOADS Profiling

## Table Overview
- Source table: `DE_PROJECT.STAGING.STG_LOADS`
- Grain: One row represents one load.
- Business key: `load_id`.

## Relationships
- One row represents one load.
- `load_id` is the business key.
- Each load belongs to one customer.
- A customer can have multiple loads.

## Data Quality Findings
- `load_id` is unique and contains no duplicates.
- `booking_type` contains three valid values:
  - Spot
  - Contract
  - Dedicated

## Transformations
- Trim identifier columns:
  - `load_id`
  - `customer_id`
  - `route_id`
- Cast `load_date` to `DATE`.
- Cast numeric columns to appropriate numeric types.
- Trim categorical columns (`load_status`, `booking_type`, `load_type`) for consistency.

## dbt Tests
- `load_id`: `unique`, `not_null`
- `customer_id`: `not_null`
- `load_date`: `not_null`
- `booking_type`: `accepted_values`
# STG_TRIPS Profiling

## Table Overview

The `STG_TRIPS` table contains operational trip-level information for freight transportation. Each record represents a single trip and includes the assigned load, driver, truck, trailer, dispatch date, operational metrics, and trip status.

---

## Grain

**One row represents one trip.**

---

## Business Key

**Business Key:** `trip_id`

The `trip_id` uniquely identifies each trip in the dataset.

---

## Relationships

| Relationship | Cardinality |
|--------------|-------------|
| Driver → Trips | One-to-Many |
| Truck → Trips | One-to-Many |
| Trailer → Trips | One-to-Many |
| Load → Trips | One-to-Many |
| Trip → Driver | One-to-One |
| Trip → Truck | One-to-One |
| Trip → Trailer | One-to-One |
| Trip → Load | One-to-One |

---

## Data Quality Findings

### Primary Key

- `trip_id` is unique.
- No duplicate trip IDs were identified.
- No missing (`NULL`) values were found.

### Missing Values

The following columns contained blank (empty string/whitespace) values instead of SQL `NULL` values:

- `driver_id`
- `truck_id`
- `trailer_id`

These values will be standardized during staging using:

```sql
NULLIF(TRIM(column_name), '')
```

This converts blank strings into SQL `NULL` values for consistent downstream processing.

### Trip Status

Only one status value exists in the dataset:

- `COMPLETE`

No unexpected status values were identified.

---

## Transformations

The following transformations are applied in the staging model:

- Trim leading and trailing whitespace from text columns.
- Convert blank strings to `NULL` using `NULLIF(TRIM(column), '')` for:
  - `driver_id`
  - `truck_id`
  - `trailer_id`
- Cast `dispatch_date` to `DATE`.
- Cast numeric columns to appropriate numeric data types.

---

## dbt Tests

### `trip_id`

- `unique`
- `not_null`

### `dispatch_date`

- `not_null`

### `trip_status`

- `accepted_values`
  - `COMPLETE`

No `not_null` tests are currently applied to:

- `driver_id`
- `truck_id`
- `trailer_id`

because the source data contains missing values represented as blank strings. These are standardized to `NULL` during staging.

---

## Summary

The `STG_TRIPS` table is a trip-level operational dataset where `trip_id` serves as the business key. Profiling confirmed one-to-many relationships between drivers, trucks, trailers, loads, and trips. The primary data quality issue identified was the presence of blank strings in identifier columns, which are standardized to `NULL` during staging. The table is suitable for downstream dimensional modelling after these standardization steps.
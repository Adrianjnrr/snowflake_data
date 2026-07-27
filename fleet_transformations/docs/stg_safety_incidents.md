# STG_SAFETY_INCIDENTS_CLEAN

## Overview

The `stg_safety_incidents_clean` model cleans and standardizes raw safety incident data by removing unnecessary whitespace, standardizing blank values, converting data types, and preparing the dataset for downstream analytical models.

---

## Grain

**One row represents one safety incident.**

---

## Business Key

**incident_id**

Each safety incident is uniquely identified by `incident_id`.

---

## Relationships

- One driver can be associated with many safety incidents.
- One truck can be associated with many safety incidents.
- One trip can be associated with many safety incidents.

---

## Data Quality Findings

### incident_id
- No duplicate records found.
- No NULL values.
- Suitable business key.

### driver_id
- Blank strings were found in the raw data.
- Blank values were converted to SQL `NULL` using:

```sql
NULLIF(TRIM(driver_id), '') AS driver_id
```

- One record contains a NULL `driver_id` after cleaning.
- This was identified by the dbt `not_null` test and flagged as a data quality issue.

### incident_date
- No NULL values.
- Converted to `DATE`.

### incident_type
- No NULL values.
- Leading and trailing whitespace removed.

### description
- No NULL values.
- Leading and trailing whitespace removed.

### injury_flag
- Converted to `BOOLEAN`.
- No NULL values.

### at_fault_flag
- Converted to `BOOLEAN`.

### preventable_flag
- Converted to `BOOLEAN`.
- No NULL values.

### vehicle_damage_cost
- Converted to `FLOAT`.
- NULL values are acceptable where no vehicle damage occurred.

### cargo_damage_cost
- Converted to `FLOAT`.
- NULL values are acceptable where no cargo damage occurred.

### claim_amount
- Converted to `FLOAT`.
- NULL values are acceptable where no insurance claim exists.

### location_city
- Leading and trailing whitespace removed.

### location_state
- Leading and trailing whitespace removed.

---

## Transformations

| Column | Transformation |
|---------|----------------|
| incident_id | `TRIM()` |
| trip_id | `TRIM()` |
| driver_id | `NULLIF(TRIM(driver_id), '')` |
| truck_id | `TRIM()` |
| incident_date | `CAST(... AS DATE)` |
| incident_type | `TRIM()` |
| location_city | `TRIM()` |
| location_state | `TRIM()` |
| at_fault_flag | `CAST(... AS BOOLEAN)` |
| injury_flag | `CAST(... AS BOOLEAN)` |
| vehicle_damage_cost | `CAST(... AS FLOAT)` |
| cargo_damage_cost | `CAST(... AS FLOAT)` |
| claim_amount | `CAST(... AS FLOAT)` |
| preventable_flag | `CAST(... AS BOOLEAN)` |
| description | `TRIM()` |

---

## dbt Tests

| Column | Test | Status |
|---------|------|--------|
| incident_id | `unique` | ✅ Pass |
| incident_id | `not_null` | ✅ Pass |
| incident_date | `not_null` | ✅ Pass |
| driver_id | `not_null` | ❌ Fail (1 record) |
| incident_type | `not_null` | ✅ Pass |
| description | `not_null` | ✅ Pass |
| injury_flag | `not_null` | ✅ Pass |
| preventable_flag | `not_null` | ✅ Pass |

---

## Data Quality Issues

| Issue | Status |
|------|--------|
| One safety incident contains a missing `driver_id` after converting blank strings to NULL. | Identified by dbt |
| No duplicate `incident_id` values. | Resolved |
| No missing `incident_date` values. | Passed |
| No missing `incident_type` values. | Passed |
| No missing `description` values. | Passed |
| No missing `injury_flag` values. | Passed |
| No missing `preventable_flag` values. | Passed |
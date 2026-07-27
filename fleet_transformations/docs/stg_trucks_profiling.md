# STG_TRUCKS Profiling

## Table Grain

- One row represents one trip.

## Business Key

- trip_id

## Findings

- trip_id is unique.
- truck_id is not unique because a truck can perform multiple trips.
- driver_id is not unique because a driver can complete multiple trips.
- dispatch_date is stored as VARCHAR.
- Numeric metrics are stored as VARCHAR.

## Data Quality Issues

- Approximately 1,600 records have missing truck_id.
- Some records have missing driver_id.
- truck_id duplicates are expected because trucks perform multiple trips.

## Transformations

- CAST dispatch_date to DATE.
- CAST distance, duration, MPG, fuel and idle time to FLOAT.
- TRIM ID columns.
- Standardise trip_status if necessary.

## dbt Tests

- trip_id → unique
- trip_id → not_null
- dispatch_date → not_null
- truck_id → not_null (expected to fail because of existing data quality issues)
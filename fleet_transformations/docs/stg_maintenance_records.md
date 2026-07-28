# STG_MAINTENANCE_RECORDS

## Grain
One row represents one maintenance record.

## Business Key
- `maintenance_id`

## Relationships
- One truck → Many maintenance records
- One maintenance record → One truck

## Data Quality Checks
- ✅ No duplicate `maintenance_id`
- ✅ Checked for NULL values
- ✅ Checked leading/trailing whitespace
- ✅ Checked date range (MIN/MAX)
- ✅ Checked numeric columns for negative values

## Transformations
- `TRIM()` text columns
- `NULLIF(TRIM(column), '')` for blank strings
- Cast columns to appropriate data types

## dbt Tests
- `maintenance_id`
  - `unique`
  - `not_null`
- `maintenance_date`
  - `not_null`
# STG_FUEL_PURCHASES

## Grain
One row represents one fuel purchase transaction.

## Business Key
- `fuel_purchase_id`

## Relationships
- One driver → Many fuel purchases
- One truck → Many fuel purchases
- One fuel purchase → One driver
- One fuel purchase → One truck

## Data Quality Checks
- ✅ No duplicate `fuel_purchase_id`
- ✅ Checked for NULL values
- ✅ Checked leading/trailing whitespace
- ✅ Checked date range (MIN/MAX)
- ✅ Checked numeric columns for negative values

## Transformations
- `TRIM()` text columns
- `NULLIF(TRIM(column), '')` for blank strings
- Cast columns to appropriate data types

## dbt Tests
- `fuel_purchase_id`
  - `unique`
  - `not_null`
- `purchase_date`
  - `not_null`
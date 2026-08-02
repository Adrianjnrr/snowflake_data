select 
trim(truck_id) as truck_id,
trim(unit_number) as unit_number,
trim(vin) as vin,
trim(make) as make,
trim(cast(model_year as string)) as model_year,
trim(cast(acquisition_date as date)) as acquisition_date,
trim(cast(acquisition_mileage as int)) as acquisition_mileage,
cast(fuel_type as string) as fuel_type,
trim(status) as status,
trim(home_terminal) as home_terminal

from {{ source('staging', 'STG_TRUCKS')}}
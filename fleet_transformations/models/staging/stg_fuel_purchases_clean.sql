select
trim(fuel_purchase_id) as fuel_purchase_id,
trim(trip_id) as trip_id,
trim(driver_id) as driver_id,
trim(truck_id) as truck_id,
cast(trim(purchase_date) as date) as purchase_date,
cast(trim(gallons) as float) as gallons,
trim(location_city) as location_city,
trim(location_state) as location_state,
cast(trim(price_per_gallon) as float) as price_per_gallon,
cast(trim(total_cost) as float) as total_cost,
trim(fuel_card_number) as fuel_card_number

from {{ source('staging', 'STG_FUEL_PURCHASES') }}
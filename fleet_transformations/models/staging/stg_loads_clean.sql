select 
trim(load_id) as load_id,
trim(customer_id) as customer_id,
trim(route_id) as route_id,
cast(accessorial_charges as int) as accessorial_charges,
cast(load_date as date) as load_date,
trim(load_type) as load_type,
cast(weight_lbs as int) as weight_lbs,
cast(pieces as int) as pieces,
cast(revenue as float) as revenue,
cast(fuel_surcharge as float) as fuel_surcharge,
trim(load_status) as load_status,
trim(booking_type) as booking_type

from {{ source('staging', 'STG_LOADS')}}
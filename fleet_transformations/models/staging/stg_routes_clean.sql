select
trim(route_id) as route_id,
trim(origin_city) as origin_city,
trim(origin_state) as origin_state,
trim(destination_city) as destination_city,
trim(destination_state) as destination_state,
cast(typical_distance_miles as int) as typical_distance_miles,
cast(base_rate_per_mile as float) as base_rate_per_miles,
cast(fuel_surcharge_rate as float) as fuel_surcharge_rate,
cast(typical_transit_days as int) as typical_transit_days

from {{ source('staging', 'STG_ROUTES') }}
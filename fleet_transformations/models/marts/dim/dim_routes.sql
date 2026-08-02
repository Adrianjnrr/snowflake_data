select
route_id,
origin_city,
origin_state,
destination_city,
destination_state,
typical_distance_miles,
base_rate_per_miles,
fuel_surcharge_rate,
typical_transit_days
from {{ ref('stg_routes_clean') }}
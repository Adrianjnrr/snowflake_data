select r.route_id,
r.origin_city,
r.origin_state,
r.destination_city,
r.destination_state,
r.typical_distance_miles,
r.base_rate_per_miles,
r.fuel_surcharge_rate,
r.typical_transit_days,
l.load_id,
l.customer_id,
l.load_type,
l.load_date,
l.revenue,
l.load_status

from {{ ref('stg_routes_clean') }} r
left join {{ ref('stg_loads_clean') }} l
on r.route_id = l.route_id
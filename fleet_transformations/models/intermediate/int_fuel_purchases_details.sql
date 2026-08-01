select f.fuel_purchase_id,
f.trip_id,
f.driver_id, 
f.truck_id,
f.purchase_date,
f.gallons,
f.location_city,
f.location_state,
f.price_per_gallon,
f.total_cost,
f.fuel_card_number,
t.fuel_gallon_used,
d.first_name,
d.last_name,
d.employment_status

from {{ ref('stg_fuel_purchases_clean') }} f
left join {{ ref('stg_trips_clean') }} t
on f.trip_id = t.trip_id
left join {{ ref('stg_drivers_clean') }} d
on f.driver_id = d.driver_id

select
trip_id,
load_id,
driver_id,
trailer_id,
truck_id,
customer_id,
route_id,

dispatch_date,

actual_distance_miles,
actual_duration_hours,
fuel_gallon_used,
average_mpg,
idle_time_hours,

trip_status

from {{ ref('int_trips_details') }}
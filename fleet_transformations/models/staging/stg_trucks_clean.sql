select 
trim(trip_id) as trip_id,
trim(truck_id) as truck_id,
trim(driver_id) as driver_id,
trim(load_id) as load_id,
trim(trailer_id) as trailer_id,

cast(dispatch_date as date) as dispatch_date,
cast(actual_distance_miles as float) as actual_distance_miles,
cast(actual_duration_hours as float) as actual_duration_hours,
cast(fuel_gallons_used as float) as fuel_gallons_used,
cast(average_mpg as float) as average_mpg,
cast(idle_time_hours as float) as idle_time_hours

from {{ source('staging', 'STG_TRUCKS')}}
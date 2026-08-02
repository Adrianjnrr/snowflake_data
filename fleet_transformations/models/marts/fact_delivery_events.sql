select 
facility_id,
event_id,
detention_minutes,
on_time_flag,
temperature,
precipitation,
wind_speed,
relative_humidity
from {{ ref('int_facilities_details') }}
select f.facility_id,
f.facility_name,
f.facility_type,
f.city,
f.state,
f.latitude,
f.longitude,
f.dock_doors,
f.operating_hours,
d.event_id,
d.event_type,
d.scheduled_datetime,
d.actual_datetime,
d.detention_minutes,
d.on_time_flag,
d.location_city,
d.location_state,
w.precipitation,
w.temperature,
w.weather_time,
w.wind_speed,
w.relative_humidity

from {{ ref('stg_facilities_clean') }} f
left join {{ ref('stg_delivery_events_clean') }} d
on f.facility_id = d.facility_id
left join {{ ref('stg_weather_clean') }} w
on f.facility_id = w.facility_id
and date_trunc('hour', d.actual_datetime) = date_trunc('hour', w.weather_time)
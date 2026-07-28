select
trim(event_id) as event_id,
trim(load_id) as load_id,
trim(trip_id) as trip_id,
trim(event_type) as event_type,
trim(facility_id) as facility_id,
cast(trim(scheduled_datetime) as date) as scheduled_datetime,
cast(trim(actual_datetime) as date) as actual_datetime,
cast(trim(detention_minutes) as int) as detention_minutes,
trim(on_time_flag) as on_time_flag,
trim(location_city) as location_city,
trim(location_state) as location_state

from {{ source('staging', "STG_DELIVERY_EVENTS")}}

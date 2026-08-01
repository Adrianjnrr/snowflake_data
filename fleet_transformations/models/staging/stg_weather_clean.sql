select
trim(facility_id) as facility_id,
trim(facility_name) as facility_name,
trim(city) as city,
trim(state) as state,
cast(trim(latitude) as float) as latitude,
cast(trim(longitude) as float) as longitude,
cast(trim(weather_time) as date) as weather_time,
cast(trim(temperature_2M) as float) as temperature,
cast(trim(precipitation) as float) as precipitation,
cast(trim(wind_speed_10M) as float) as wind_speed,
cast(trim(relative_humidity_2M) as int) as relative_humidity

from {{ source('staging', "STG_WEATHER")}}
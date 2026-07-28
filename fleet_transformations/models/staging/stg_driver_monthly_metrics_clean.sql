select
trim(driver_id) as driver_id,
cast(trim(month) as date) as month,
cast(trim(trips_completed) as int) as trips_completed,
cast(trim(total_miles) as float) as total_miles,
cast(trim(total_revenue) as float) as total_revenue,
cast(trim(average_mpg) as float) as average_mpg,
cast(trim(total_fuel_gallons) as float) as total_fuel_gallons,
cast(trim(on_time_delivery_rate) as float) as on_time_delivery_rate,
cast(trim(average_idle_hours) as float) as average_idle_hours

from {{ source('staging', 'STG_DRIVER_MONTHLY_METRICS') }}



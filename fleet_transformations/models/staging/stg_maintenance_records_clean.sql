select
trim(maintenance_id) as maintenance_id,
trim(truck_id) as truck_id,
cast(trim(maintenance_date) as date) as maintenance_date,
trim(maintenance_type) as maintenance_type,
cast(trim(odometer_reading) as integer) as odometer_reading,
cast(trim(labor_hours) as float) as labor_hours,
cast(trim(labor_cost) as float) as labor_cost,
cast(trim(parts_cost) as float) as parts_cost,
cast(trim(total_cost) as float) as total_cost,
trim(facility_location) as facility_location,
cast(trim(downtime_hours) as float) as downtime_hours,
trim(service_description) as service_description

from {{ source('staging', 'STG_MAINTENANCE_RECORDS') }}
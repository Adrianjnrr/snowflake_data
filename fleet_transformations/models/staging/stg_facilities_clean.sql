select
trim(facility_id) as facility_id,
trim(facility_name) as facility_name,
trim(facility_type) as facility_type,
trim(city) as city,
trim(state) as state,
cast(trim(latitude) as float) as latitude,
cast(trim(longitude) as float) as longitude,
cast(trim(dock_doors) as int) as dock_doors,
trim(operating_hours) as operating_hours
from {{ source('staging', 'STG_FACILITIES') }}

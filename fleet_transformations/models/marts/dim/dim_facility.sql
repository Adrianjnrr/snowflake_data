select
facility_id,
facility_name,
facility_type,
city,
state,
latitude,
longitude,
dock_doors,
operating_hours
from {{ ref('stg_facilities_clean') }}
select m.maintenance_id,
m.maintenance_date,
m.maintenance_type,
m.labor_hours,
m.labor_cost,
m.parts_cost,
m.total_cost,
m.facility_location,
m.downtime_hours,
m.service_description,
t.truck_id

from {{ ref('stg_maintenance_records_clean') }} m
left join {{ ref('stg_trucks_clean') }} t
on m.truck_id = t.truck_id
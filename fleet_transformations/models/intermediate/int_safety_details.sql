select i.incident_id,
t.trip_id,
i.driver_id,
i.truck_id,
i.incident_type,
i.incident_date,
i.location_city,
i.location_state,
i.vehicle_damage_cost,
i.claim_amount,
i.preventable_flag,
i.description,
d.first_name,
d.last_name,
d.employment_status

from {{ ref('stg_safety_incidents_clean') }} i
left join {{ ref('stg_trips_clean') }} t
on i.trip_id = t.trip_id
left join {{ ref('stg_drivers_clean') }} d
on i.driver_id = d.driver_id
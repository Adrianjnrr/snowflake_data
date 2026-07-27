select
trim(incident_id) as incident_id,
trim(trip_id) as trip_id,
nullif(trim(driver_id),'') as driver_id,
trim(truck_id) as truck_id,

cast(incident_date as date) as incident_date,
trim(incident_type) as incident_type,
trim(location_city) as location_city,
trim(location_state) as location_state,

cast(at_fault_flag as boolean) as at_fault_flag,
cast(injury_flag as boolean) as injury_flag,
cast(vehicle_damage_cost as float) as vehicle_damage_cost,
cast(cargo_damage_cost as float) as cargo_damage_cost,
cast(claim_amount as float) as claim_amount,
cast(preventable_flag as boolean) as preventable_flag,
trim(description) as description

from {{ source('staging', 'STG_SAFETY_INCIDENTS')}}
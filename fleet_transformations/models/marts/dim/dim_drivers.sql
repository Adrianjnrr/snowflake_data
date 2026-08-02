select
driver_id,
first_name,
last_name,
license_number,
license_state,
hire_date,
employment_status

from {{ ref('stg_drivers_clean') }}
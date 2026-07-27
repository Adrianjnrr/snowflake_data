SELECT  
driver_id,
first_name,
last_name,
license_number,
license_state,
termination_date,
cast(date_of_birth as date) as date_of_birth,
cast(hire_date as date) as hire_date,
home_terminal,
cdl_class,
years_experience,
employment_status

FROM {{ source('staging', 'STG_DRIVERS') }}
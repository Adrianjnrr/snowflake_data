select
trailer_id,
trailer_type,
trailer_number,
model_year,
vin,
status,
current_location

from {{ ref('stg_trailers_clean') }}
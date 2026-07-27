select
trim(trailer_id) as trailer_id,
trim(trailer_type) as trailer_type,
cast(trailer_number as int) as trailer_number,
cast(length_feet as int) as length_feet,
cast(model_year as date) as model_year,
trim(vin) as vin,
cast(acquisition_date as date) as acquisition_date,
trim(status) as status,
trim(current_location) as current_location

from {{ source('staging', 'STG_TRAILERS')}}



SELECT *
FROM {{ source('staging', 'STG_TRIPS') }}
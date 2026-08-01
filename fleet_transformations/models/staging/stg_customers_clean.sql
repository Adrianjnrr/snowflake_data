select
trim(customer_id) as customer_id,
trim(customer_name) as customer_name,
trim(customer_type) as customer_type,
cast(trim(credit_terms_days) as int) as credit_terms_days,
trim(primary_freight_type) as primary_freight_type,
trim(account_status) as account_status,
cast(trim(contract_start_date) as date) as contract_start_date,
cast(trim(annual_revenue_potential) as int) as annual_revenue_potential

from {{ source('staging', "STG_CUSTOMERS") }}
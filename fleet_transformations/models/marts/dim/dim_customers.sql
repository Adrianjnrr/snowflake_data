select 
customer_id,
customer_name,
customer_type,
account_status,
contract_start_date,
primary_freight_type,
annual_revenue_potential
from {{ ref('stg_customers_clean') }}
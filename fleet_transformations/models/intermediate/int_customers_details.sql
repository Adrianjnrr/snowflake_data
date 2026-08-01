select c.customer_id,
c.customer_name,
c.customer_type,
c.account_status,
l.load_id,
l.load_type,
l.load_status,
l.load_date,
l.revenue,
l.booking_type,
c.primary_freight_type,
c.credit_terms_days,
c.contract_start_date,
c.annual_revenue_potential

from {{ ref('stg_customers_clean') }} c
left join {{ ref('stg_loads_clean') }} l
on c.customer_id = l.customer_id

with subscriptions as (

    select
        customer_id,
        start_date,
        end_date
    from {{ ref('stg_subscriptions') }}

),

churned as (

    select
        date_trunc('month', end_date) as month,
        count(distinct customer_id) as churned_customers
    from subscriptions
    where end_date is not null
    group by 1

)

select *
from churned
order by month
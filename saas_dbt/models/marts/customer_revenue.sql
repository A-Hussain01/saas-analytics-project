with customers as (

    select *
    from {{ ref('stg_customers') }}

),

subscriptions as (

    select *
    from {{ ref('stg_subscriptions') }}

),

payments as (

    select *
    from {{ source('raw','payments_raw') }}

),

customer_revenue as (

    select
        c.customer_id,
        c.country,
        count(distinct s.subscription_id) as subscriptions,
        sum(p.amount) as total_revenue

    from customers c

    left join subscriptions s
        on c.customer_id = s.customer_id

    left join payments p
        on c.customer_id = p.customer_id

    group by 1,2

)

select *
from customer_revenue
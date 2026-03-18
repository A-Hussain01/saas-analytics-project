with payments as (

    select
        customer_id,
        date_trunc('month', payment_date) as month,
        sum(amount) as revenue

    from {{ source('raw','payments_raw') }}

    group by 1,2

)

select
    month,
    sum(revenue) as mrr
from payments
group by 1
order by 1
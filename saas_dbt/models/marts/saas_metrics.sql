with mrr as (

    select *
    from {{ ref('mrr') }}

),

churn as (

    select *
    from {{ ref('churn_rate') }}

),

combined as (

    select
        m.month,
        m.mrr,
        coalesce(c.churned_customers,0) as churned_customers

    from mrr m

    left join churn c
        on m.month = c.month

)

select *
from combined
order by month
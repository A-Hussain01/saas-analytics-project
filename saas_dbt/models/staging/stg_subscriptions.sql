with source_data as (

    select
        subscription_id,
        customer_id,
        plan_id,
        start_date,
        end_date
    from {{ source('raw','subscriptions_raw') }}

)

select *
from source_data
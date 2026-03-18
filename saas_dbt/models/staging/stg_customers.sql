with source_data as (

    select
        customer_id,
        initcap(first_name) as first_name,
        initcap(last_name) as last_name,
        lower(email) as email,
        country,
        signup_date
    from {{ source('raw','customers_raw') }}

)

select *
from source_data
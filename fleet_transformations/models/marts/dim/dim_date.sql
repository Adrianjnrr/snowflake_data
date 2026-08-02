with dates as (

    select
        dateadd(day, seq4(), '2022-01-01') as full_date
    from table(generator(rowcount => 7305))

)

select

    to_number(to_char(full_date, 'YYYYMMDD')) as date_key,

    full_date,

    year(full_date) as year,

    quarter(full_date) as quarter,

    month(full_date) as month,

    monthname(full_date) as month_name,

    week(full_date) as week,

    day(full_date) as day,

    dayname(full_date) as weekday_name,

    case
        when dayofweek(full_date) in (0,6) then true
        else false
    end as is_weekend

from dates
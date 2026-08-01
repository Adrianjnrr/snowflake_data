
select t.trip_id,
       t.load_id,
       t.driver_id,
       t.trailer_id,
       t.truck_id,
       d.first_name,
       d.last_name,
       t.dispatch_date,
       trl.trailer_type,
       trl.trailer_number,
       trl.status,
       l.customer_id,
       l.route_id,
       l.load_date,
       l.load_type,
       l.load_status,
       l.booking_type,
       t.actual_distance_miles,
       t.actual_duration_hours,
       t.fuel_gallon_used,
       t.average_mpg,
       t.idle_time_hours,
       t.trip_status,
       d.license_number

       from {{ ref('stg_trips_clean') }} t
       left join {{ ref('stg_drivers_clean') }} d
       on t.driver_id = d.driver_id
         left join {{ ref('stg_trailers_clean') }} trl
            on t.trailer_id = trl.trailer_id
        left join {{ ref('stg_loads_clean') }} l
            on t.load_id = l.load_id
        
       



       
       
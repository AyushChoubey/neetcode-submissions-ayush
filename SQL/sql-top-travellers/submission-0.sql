-- Write your query below
with a as(select user_id,sum(distance)as travelled_distance  from rides group by user_id )

,b as (select name,coalesce(travelled_distance,0) as travelled_distance   from users as u left join a on u.id = a.user_id)
select name,travelled_distance from b  order by travelled_distance desc , name
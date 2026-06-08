-- Write your query below
select u.name, coalesce(sum(r.distance),0) as travelled_distance
from users u
Left join rides as r
on r.user_id = u.id
group by u.id,u.name
ORDER BY travelled_distance DESC, u.name ASC;
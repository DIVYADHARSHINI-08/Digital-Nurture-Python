select count(distinct Users.user_id) , Users.city
from Users
inner join Registrations
on Users.user_id = Registrations.user_id
group by Users.city
order by COUNT(DISTINCT Users.user_id) DESC limit 5;
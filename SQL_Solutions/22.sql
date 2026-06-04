select Users.full_name ,count(distinct Registrations.event_id)
from Users
left join Registrations 
on Registrations.user_id = Users.user_id
GROUP BY Users.full_name
HAVING COUNT(DISTINCT Registrations.event_id) > 1;
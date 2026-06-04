select Users.full_name,count(Events.event_id),Events.status
from Events
inner join Users
on Events.organizer_id = Users.user_id
Group by Users.full_name , Events.status 
order by Users.full_name;
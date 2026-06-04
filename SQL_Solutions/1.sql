select events.title,events.city,events.description,events.start_date,events.end_date,events.status
from events
inner join registrations
on registrations.event_id = events.event_id
inner join users
on users.user_id = registrations.user_id
where Events.status = 'upcoming'
AND Users.city = Events.city
order by start_date;
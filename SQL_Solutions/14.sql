select Events.title,Count(Registrations.event_id)
from Events
inner join Registrations
on Registrations.event_id = Events.event_id
group by Events.title
order by Count(Registrations.event_id) desc limit 3;
select Events.event_id,Events.title,count(Resources.resource_id)
from Resources
inner join Events 
on Resources.event_id = Events.event_id
Group by Events.event_id,Events.title;
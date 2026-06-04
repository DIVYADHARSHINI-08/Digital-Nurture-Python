select Events.event_id,COUNT(Sessions.session_id)
from Events
left join Sessions
on Events.event_id = Sessions.event_id
Where Events.status = 'upcoming'
Group by Events.event_id ;
Select Events.title
from Events
left join Sessions
on Sessions.event_id = Events.event_id
where Sessions.session_id is null;
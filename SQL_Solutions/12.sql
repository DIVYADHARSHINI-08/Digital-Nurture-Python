select Count(Sessions.session_id),Events.event_id,Events.title
from Sessions
inner join Events
on Events.event_id = Sessions.event_id
group by Events.event_id,Events.title
order by Count(Sessions.session_id) Desc limit 1;
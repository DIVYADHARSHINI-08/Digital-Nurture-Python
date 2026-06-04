select Events.event_id,Events.title,Count(Sessions.session_id) as "Total Sessions"
from Events
inner join Sessions
on Events.event_id = Sessions.event_id
where time(Sessions.start_time) between '10:00:00' and '12:00:00'
group by Events.event_id,Events.title;
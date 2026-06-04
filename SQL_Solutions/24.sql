select avg(TIMESTAMPDIFF(MINUTE, start_time, end_time)),Sessions.event_id
from Sessions
group by Sessions.event_id;
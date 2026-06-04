select Events.title
from Events
left join Resources
on Events.event_id = Resources.event_id
where Resources.event_id is Null;
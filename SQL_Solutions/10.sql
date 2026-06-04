select Events.title
from Events 
inner join Registrations 
on Registrations.event_id = Events.event_id
left join Feedback
on Events.event_id = Feedback.event_id
where Feedback.event_id is null
Group by Events.title;
select count(DISTINCT Registrations.registration_id) , AVG(Feedback.rating) , Events.title
from Events
left join Registrations 
on Registrations.event_id = Events.event_id
left join Feedback 
on Feedback.event_id = Events.event_id
where Events.status = "completed"
group by Events.title;

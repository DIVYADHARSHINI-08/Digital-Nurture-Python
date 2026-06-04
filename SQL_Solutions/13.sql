select avg(Feedback.rating),Events.city
from Events
inner join Feedback
on Feedback.event_id = Events.event_id
group by Events.city;

select Users.full_name,Feedback.rating,Feedback.comments,Events.title
from Feedback
inner join Users
on Users.user_id = Feedback.user_id
inner join Events
on Feedback.event_id = Events.event_id
where Feedback.rating < 3;
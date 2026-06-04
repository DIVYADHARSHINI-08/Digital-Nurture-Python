select Users.full_name , Count(DISTINCT Registrations.event_id) , count(distinct Feedback.feedback_id)
from Users 
left join Registrations
on Registrations.user_id = Users.user_id
left join Feedback 
on Feedback.user_id = Users.user_id
group by Users.user_id;

select Users.full_name , count(distinct Feedback.feedback_id)
from Users
left join Feedback 
on Feedback.user_id = Users.user_id
group by Users.full_name
order by count(distinct Feedback.feedback_id) desc limit 5;
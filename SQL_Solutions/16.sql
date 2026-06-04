select Users.user_id ,Users.full_name
from Users
left join Registrations
on Registrations.user_id = Users.user_id
where Users.registration_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
and Registrations.user_id IS NULL;

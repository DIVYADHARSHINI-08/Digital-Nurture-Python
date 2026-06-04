select count(Users.user_id),Users.registration_date
from Users
where registration_date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
group by Users.registration_date;
select * from Users
left join Registrations on  Users.user_id = Registrations.user_id
and DATE_SUB(CURDATE(), INTERVAL 90 DAY)
where Registrations.user_id is null;
select month(Registrations.registration_date), count(distinct Registrations.registration_id)
from Registrations
WHERE registration_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
group by month(Registrations.registration_date)
ORDER BY MONTH(Registrations.registration_date);
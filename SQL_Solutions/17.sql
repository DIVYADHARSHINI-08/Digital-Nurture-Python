select speaker_name , count(session_id)
from Sessions
group by speaker_name
having count(session_id) > 1;
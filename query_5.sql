select t.name, d.name
from teachers t 
join disciplines d on d.teacher_id = t.id
where t.id = 1;
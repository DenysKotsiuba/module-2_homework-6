select d.name
from grades g 
join disciplines d on d.id = g.disciplines_id 
join students s on s.id = g.students_id 
where s.id = 1
group by d.name;
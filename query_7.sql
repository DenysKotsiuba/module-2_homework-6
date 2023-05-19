select gr.name, d.name, s.name, g.grade
from grades g 
join disciplines d on d.id = g.disciplines_id 
join students s on s.id = g.students_id 
join "groups" gr on gr.id = s.group_id 
where gr.id = 1 and d.id = 1
order by s.name, g.grade desc;
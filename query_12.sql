select gr.name, s.name, d.name, g.grade, g.date_of 
from grades g 
join disciplines d on d.id = g.disciplines_id 
join students s on s.id = g.students_id 
join "groups" gr on gr.id = s.group_id 
where gr.id = 1 and d.id = 1 and g.date_of = (select max(g.date_of)
	from grades g 
	join disciplines d on d.id = g.disciplines_id 
	join students s on s.id = g.students_id 
	join "groups" gr on gr.id = s.group_id 
	where gr.id = 1 and d.id = 1);
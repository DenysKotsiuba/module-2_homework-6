select t.name, s.name, round(avg(g.grade), 2) as average_grade
from grades g 
join disciplines d on d.id = g.disciplines_id 
join teachers t on t.id = d.teacher_id 
join students s on s.id = g.students_id 
where t.id = 1 and s.id = 1
group by t.name, s.name;
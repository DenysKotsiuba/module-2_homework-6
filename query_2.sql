select d.name, s.name, round(avg(g.grade), 2) as average_grade
from grades g
join disciplines d on d.id = g.disciplines_id
join students s on s.id = g.students_id
where d.id = 1
group by d.name, s.name
order by average_grade desc
limit 1;
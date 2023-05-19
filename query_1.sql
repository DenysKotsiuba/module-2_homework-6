select s.name, round(avg(g.grade), 2) as average_grade
from students as s
join grades as g on g.students_id = s.id
group by s.id
order by average_grade desc
limit 5;
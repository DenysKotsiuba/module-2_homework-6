select s.name, gr.name
from students s 
join "groups" gr on gr.id = s.group_id 
where gr.id = 3;
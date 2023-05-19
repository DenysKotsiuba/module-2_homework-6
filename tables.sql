drop table if exists groups cascade;
create table groups (
	id smallserial primary key,
	name varchar(20) unique
);

drop table if exists teachers cascade;
create table teachers(
	id smallserial primary key,
	name varchar(50) not null
);

drop table if exists students cascade;
create table students(
	id smallserial primary key,
	name varchar(50) not null,
	group_id smallserial,
	foreign key (group_id) references groups(id)
		on delete set null
		on update cascade 
);

drop table if exists disciplines cascade;
create table disciplines(
	id smallserial primary key,
	name varchar(50) not null unique,
	teacher_id smallserial,
	foreign key (teacher_id) references teachers(id)
		on delete set null 
		on update cascade 
);

drop table if exists grades cascade;
create table grades(
	id smallserial primary key,
	grade smallint,
	date_of date not null,
	students_id smallserial,
	disciplines_id smallserial,
	foreign key (students_id) references students(id)
		on delete set null 
		on update cascade,
	foreign key (disciplines_id) references disciplines(id)
		on delete set null 
		on update cascade
);

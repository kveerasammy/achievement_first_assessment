
CREATE TABLE assessment.student_grades
(
    student_id integer,
    name character varying(50) COLLATE pg_catalog."default",
    quiz character varying(50) COLLATE pg_catalog."default",
    administrationdate date,
    score integer
)
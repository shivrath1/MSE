## ER Diagram

The ER diagram is the relationship between students and courses.

- A student can enroll in multiple courses.
- A course can have multiple students.
- A Lecturer teaches one or more courses.
- Each course is associated with one lecturer.
- The enrollment entity represents this many-to-many relationship and connects using foreign keys (studentId and courseId).

The Lecturer entity includes:
- lecturerId (Primary Key)
- name
- email
- department
- contact

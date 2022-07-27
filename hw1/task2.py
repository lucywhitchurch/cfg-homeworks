"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.subjects = {}  # subject, grade
        self.marks = []  # mark

    def add_subject(self, subjects):
        self.subjects.update(subjects)

    def remove_subject(self, subjects):
        self.subjects.pop(subjects)

    def show_subjects(self):
        for subject, grade in self.subjects():
            print(f" - {subject} - {grade}")

    def overall_mark(self):
        student_overall_mark = sum(self.marks) / len(self.marks)
        return student_overall_mark


class CFGStudent(Student):

    def __init__(self, name, id, specialisation):
        super().__init__(name, id)
        self.specialisation = specialisation

x = CFGStudent("Lucy Whitchurch", 123, 'Software')

#     create new methods that manage student's subects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
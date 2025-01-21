def stats(students: dict):
    # key in students is a matriculation number as a string.
    # value is a list of tuples, where the first element is a subject as a string and the second element is a grade between 1 and 6

    # The first dictionary should be a mapping from matriculation number to the average grade of the relevant student.

    # k:subject, v:average grade of subject across student
    def subjects_average(students: dict):

        subject_grades = {}

        for subjects in students.values():
            for subject, grade in subjects:
                if subject not in subject_grades:
                    subject_grades[subject] = []
                    subject_grades[subject].append(grade)

        res = {subject: round(sum(grades) / len(grades), 2)
               for subject, grades in subject_grades.items()}
        return res

    # k:matriculation num, v:average grade of student
    def student_average(students: dict):

        res = {}

        for mat_num, subjects in students.items():
            grades = [grade for _, grade in subjects]
            res[mat_num] = round(sum(grades)/len(grades), 2)

        return res

    return (student_average(students), subjects_average(students))

    # The second dictionary should be a mapping from school subject to the average grade of all students in that subject. The average grades should be rounded to two decimal places.


raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
       "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
       "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
       }

print(stats(raw))
students, subjects = stats(raw)
print(len(students) == 3)
print(len(subjects) == 4)
print(students["12-345-678"] == 5.17)
print(subjects["Latin"] == 4.08)

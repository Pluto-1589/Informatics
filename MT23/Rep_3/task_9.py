def add_grade(grades: dict, student: int, course: str, grade: float):
    # add_grade should take four parameters: a dictionary grades, a matriculation number student, a course name course, and a grade grade.
    # The function should update the grade for the given course of the specified student.
    # If the student is not yet represented in grades, the function will need to create a new key/value pair in grades for that student.
    # Finally, the grades dictionary should be returned.

    if student not in grades:
        grades[student] = {course: grade}
    else:
        grades[student][course] = grade
    return grades


print(add_grade({},                                    111, "INF-1", 4.00))
print(add_grade({222: {"INF-1": 3.50}},                222, "PHY-2", 5.50))
print(add_grade({222: {"INF-1": 3.50}},                333, "PHY-2", 1.75))


def remove_grade(grades: dict, student: int, course: str):
    # remove_grade should take three parameters: a dictionary grades, a matriculation number student, and a course name course.
    # If the student has a grade for the specified course, that grade should be removed.
    # If no grades remain for that student, the student should be removed from grades entirely.
    # If the student is unknown or if the student hasn't received a grade for the given course, grades should be returned as-is (meaning, no actions should be taken and no errors should arise). In any case, grades should finally be returned.
    if student in grades:

        if course in grades[student]:
            del grades[student][course]

        if len(grades[student]) == 0:
            del grades[student]

    return grades


print(remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 222, "INF-1"))
print(remove_grade({222: {"INF-1": 3.50}},                222, "INF-1"))
print(remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 111, "INF-1"))
print(remove_grade({},                                    111, "INF-1"))

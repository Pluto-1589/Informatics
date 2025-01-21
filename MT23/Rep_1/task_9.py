def add_grade(grades: dict, student: int, course: str, grade: float):
    if student not in grades:
        grades[student] = {course: grade}
    else:
        grades[student][course] = grade

    return grades


print(add_grade({},                                    111, "INF-1", 4.00))
print(add_grade({222: {"INF-1": 3.50}},                222, "PHY-2", 5.50))
print(add_grade({222: {"INF-1": 3.50}},                333, "PHY-2", 1.75))


def remove_grade(grades: dict, student: int, course: str):

    if student in grades:
        if course in grades[student]:
            del (grades[student][course])
        if len(grades[student]) == 0:
            del (grades[student])

    return grades


print(remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 222, "INF-1"))
print(remove_grade({222: {"INF-1": 3.50}},                222, "INF-1"))
print(remove_grade({222: {"INF-1": 3.50, "PHY-2": 5.50}}, 111, "INF-1"))
print(remove_grade({},                                    111, "INF-1"))

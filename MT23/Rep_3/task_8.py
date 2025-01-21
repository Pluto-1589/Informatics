def register(enrollments: dict, student: int, course: str):
    # register should take three parameters: a dictionary enrollments, a matriculation number student and a course name course.
    # The function should add the course to the set of courses for the given student.
    # Note that if the given student is not represented in enrollments yet, the function will need to create a new key/value pair in enrollments for the student.
    # Finally, the enrollments dictionary should be returned.

    if student not in enrollments:
        enrollments[student] = {course}
    else:
        enrollments[student].add(course)
    return enrollments


print(register({},                        111, "INF-1"))
print(register({222: {"INF-1", "BIO-2"}}, 222, "PHY-2"))
print(register({222: {"INF-1", "BIO-2"}}, 333, "PHY-2"))


def deregister(enrollments: dict, student: int, course: str):
    # deregister should take three parameters: a dictionary enrollments, a matriculation number student and a course name course.
    # If the student is enrolled in the given course, the course name should be removed from the set of courses of the given student.
    # If no courses remain, the student should be removed from enrollments entirely.
    # If the given student is unknown or if the student is not enrolled in the given course, enrollments should simply be returned as-is (i.e., nothing should happen and no errors should occur). In any case, enrollments should finally be returned.

    if student in enrollments:

        if course in enrollments[student]:
            enrollments[student].remove(course)

        elif enrollments[student][course] == {}:
            del enrollments[student]

    return enrollments


print(deregister({222: {"INF-1", "BIO-2"}}, 222, "INF-1"))
print(deregister({222: {"INF-1"}},          222, "INF-1"))
print(deregister({222: {"INF-1", "BIO-2"}}, 111, "INF-1"))
print(deregister({},                        111, "INF-1"))

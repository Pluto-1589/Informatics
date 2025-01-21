

def register(enrollments: dict, student: int, course: str):
    # The function should add the course to the set of courses for the given student. Note that if the given student is not represented in enrollments yet, the function will need to create a new key/value pair in enrollments for the student. Finally, the enrollments dictionary should be returned.

    if student not in enrollments:
        enrollments[student] = {course}
    else:
        enrollments[student].add(course)

    return enrollments


def deregister(enrollments: dict, student: int, course: str):

    if student in enrollments:

        if course in enrollments[student]:
            enrollments[student].remove(course)

            if len(enrollments[student]) == 0:

                del enrollments[student]

    return enrollments


print(register({},                        111, "INF-1"))
print(register({222: {"INF-1", "BIO-2"}}, 222, "PHY-2"))
print(register({222: {"INF-1", "BIO-2"}}, 333, "PHY-2"))
print(deregister({222: {"INF-1", "BIO-2"}}, 222, "INF-1"))
print(deregister({222: {"INF-1"}},          222, "INF-1"))
print(deregister({222: {"INF-1", "BIO-2"}}, 111, "INF-1"))
print(deregister({},                        111, "INF-1"))

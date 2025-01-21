# Implement both functions. Change the method signatures to add parameters as specified!
# Remember to return enrollments at the end of each function!

def register(enrollments: dict, student: int, course: str):

    if student not in enrollments:
        enrollments[student] = {course}
    else:
        enrollments[student].add(course)

    return enrollments


print(register({},                        111, "INF-1"))
print(register({222: {"INF-1", "BIO-2"}}, 222, "PHY-2"))
print(register({222: {"INF-1", "BIO-2"}}, 333, "PHY-2"))


def deregister(enrollments: dict, student: int, course: str):

    if student in enrollments:

        if course in enrollments[student]:
            enrollments[student].remove(course)

            if len(enrollments[student]) == 0:

                del (enrollments[student])

    return enrollments


print(deregister({222: {"INF-1", "BIO-2"}}, 222, "INF-1"))
print(deregister({222: {"INF-1"}},          222, "INF-1"))
print(deregister({222: {"INF-1", "BIO-2"}}, 111, "INF-1"))
print(deregister({},                        111, "INF-1"))

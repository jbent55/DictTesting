from CourseGradebook import CourseGradebook

book = CourseGradebook()

book.set_score("midterm", 11111, 91.0)
book.set_score("final", 11111, 87.0)
book.set_score("final", 22222, 91.0)
val = book.get_score("midterm", 11111)
print(val)

val2 = book.get_score("midterm", 11111)
print(val2)

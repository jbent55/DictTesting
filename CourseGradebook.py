from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        self.grades = {}
        # Type any code needed here

    # Return a dict that maps students to scores
    # An entry exists for a student only if one had been assigned by set_score
    def get_assignment_scores(self, assignment_name):
        result = {}
        # Type your code here. (remove placeholder line below)
        return result

    def get_score(self, assignment_name, studentID):
        dict = self.grades[studentID][assignment_name]
        return dict



    def get_sorted_assignment_names(self):
        result = []
        # Type your code here. (remove placeholder line below)
        return result

    # get_sorted_student_ids() returns a list with all distinct student ID,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        result = []
        # Type your code here. (remove placeholder line below)
        return result

    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID matches the method argument, and returns a dict that maps
    # each assignment name to the student's score for that assignment.
    def get_student_scores(self, studentID):
        result = {}
        # Type your code here. (remove placeholder line below)
        return result

    def set_score(self, assignment_name, studentID, score):
        temp = {studentID :{ assignment_name  : score}}
        self.grades.update(temp)
        print(self.grades)

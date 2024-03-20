
class Grader:
    def __init__(self, grades: list[list[float]]):
        self.grades = grades
 
    def compute(self):
        return [self.transform_raw(self.compute_student(student))
                for student in self.grades]
 
    def compute_student(self, student_grades: list[float]):
        return sum(student_grades) / len(student_grades)
 
    def transform_raw(self, raw: float):
        if raw < 60:
            return '5.00'
        elif raw >= 60 and raw < 65:
            return '3.00'
        elif raw >= 65 and raw < 70:
            return '2.75'
        elif raw >= 70 and raw < 75:
            return '2.50'
        elif raw >= 75 and raw < 80:
            return '2.25'
        elif raw >= 80 and raw < 84:
            return '2.00'
        elif raw >= 84 and raw < 88:
            return '1.75'
        elif raw >= 88 and raw < 92:
            return '1.5'
        elif raw >= 92 and raw < 96:
            return '1.25'
        elif raw >= 96:
            return '1.00'
    

class MinGrader(Grader):
    def adjust(self):
        for student in self.grades:
            for grade in range(len(student)):
                if student[grade] < 50:
                    student[grade] = 50
        return self.grades

class CancelTheLowestGrader(Grader):
    def compute_student(self, student_grades: list[float]):
        filtered_grades = sorted(student_grades)[1:]
        return sum(filtered_grades) / len(filtered_grades)

class ExtremistGrader(Grader):
    def extreme(self, raw: float):
        if raw >= 99:
            return '1.00'
        elif raw >= 60 and raw < 90:
            return '3.00'
        elif raw < 60:
            return '5.00'
    
    def compute(self):
        return [self.extreme(self.compute_student(student))
                for student in self.grades]

class StepUpGrader(Grader):
    def up_raw(self, raw: float, n: int):
        if n < 1:
            if raw < 60:
                return '5.00'
            elif raw >= 60 and raw < 65:
                return '3.00'
            elif raw >= 65 and raw < 70:
                return '2.75'
            elif raw >= 70 and raw < 75:
                return '2.50'
            elif raw >= 75 and raw < 80:
                return '2.25'
            elif raw >= 80 and raw < 84:
                return '2.00'
            elif raw >= 84 and raw < 88:
                return '1.75'
            elif raw >= 88 and raw < 92:
                return '1.5'
            elif raw >= 92 and raw < 96:
                return '1.25'
            elif raw >= 96:
                return '1.00'
        elif n >= 1:
            step = n * 0.25
            new_raw = raw - step
            if new_raw < 60:
                return '5.00'
            elif new_raw >= 60 and new_raw < 65:
                return '3.00'
            elif new_raw >= 65 and new_raw < 70:
                return '2.75'
            elif new_raw >= 70 and new_raw < 75:
                return '2.50'
            elif new_raw >= 75 and new_raw < 80:
                return '2.25'
            elif new_raw >= 80 and new_raw < 84:
                return '2.00'
            elif new_raw >= 84 and new_raw < 88:
                return '1.75'
            elif new_raw >= 88 and new_raw < 92:
                return '1.5'
            elif new_raw >= 92 and new_raw < 96:
                return '1.25'
            elif new_raw >= 96:
                return '1.00'

grades: list[list[float]] = [[100, 100, 100, 100], [100, 0, 60, 100], [30, 100, 100, 0], [0, 0, 0, 0]]
 
x =  StepUpGrader(grades)
print(x.compute())

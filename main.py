class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self):
        sum_grade = 0
        len_grade = 0
        for grade in self.grades.values():
            grade_course = sum(grade)
            sum_grade += grade_course
            len_grade += len(grade)
        avg_grade = round(sum_grade / len_grade, 1)
        return avg_grade

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.avg_grade()}\n' \
               f'Курсы в процессе изучения: {",".join (self.courses_in_progress)}\n' \
               f'Завершенные курсы: {",". join (self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.avg_grade() <= other.avg_grade()

    def rate_mentor(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def avg_grade(self):
        sum_grade = 0
        len_grade = 0
        for grade in self.grades.values():
            grade_course = sum(grade)
            sum_grade += grade_course
            len_grade += len(grade)
        avg_grade = round(sum_grade / len_grade, 1)
        return avg_grade

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.avg_grade() <= other.avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def __eq__(self, other):
    return self.avg_grade() == other.avg_grade()


def average_grade_student(students, course):
    if len(students):
        sum_ = 0
        count = 0
        for student in students:
            if isinstance(student, Student) and student.grades and course in student.grades:
                sum_ = sum_ + sum(student.grades[course])
                count += len(student.grades[course])
        return f'Средний бал за ДЗ по {course} у студентов: {round(sum_/count, 1)}'
    else:
        return


def average_grade_lecturer(lecturers, course):
    if len(lecturers):
        sum_ = 0
        count = 0
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and lecturer.grades and course in lecturer.grades:
                sum_ = sum_ + sum(lecturer.grades[course])
                count += len(lecturer.grades[course])
        return f'Средний бал за лекции по {course} у лекторов: {round(sum_/count, 1)}'
    else:
        return


best_student = Student('Best', 'Student', 'female')
cool_student = Student('Cool', 'Student', 'male')
best_student.courses_in_progress += ['Python', 'Java', 'C']
cool_student.courses_in_progress += ['Python']

best_reviewer = Reviewer('Best', 'Reviewer')
cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Python', 'Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_reviewer.rate_hw(cool_student, 'Python', 8)
best_reviewer.rate_hw(cool_student, 'Python', 9)
best_reviewer.rate_hw(cool_student, 'Python', 10)

best_lecturer = Lecturer('Best', 'Lecturer')
cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Java', 'C']
best_lecturer.courses_attached += ['Python', 'Java']

best_student.rate_mentor(cool_lecturer, 'Java', 10)
best_student.rate_mentor(cool_lecturer, 'Java', 9)
best_student.rate_mentor(cool_lecturer, 'C', 9)
best_student.rate_mentor(cool_lecturer, 'Java', 9)

cool_student.rate_mentor(best_lecturer, 'Python', 9)
cool_student.rate_mentor(best_lecturer, 'Python', 8)
cool_student.rate_mentor(best_lecturer, 'Python', 10)
cool_student.rate_mentor(best_lecturer, 'Python', 9)

print(best_student.name, best_student.surname, best_student.grades)
print(cool_lecturer.name, cool_lecturer.surname, cool_lecturer.grades)
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(best_student >= cool_student)
print(best_lecturer < cool_lecturer)
print(best_student != cool_student)
print()
print(average_grade_lecturer([best_lecturer, cool_lecturer], 'Java'))
print(average_grade_student([best_student, cool_student], 'Python'))

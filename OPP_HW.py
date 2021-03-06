class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_lect(self, lecturer, lecture, score):
        if isinstance(lecturer, Lecturer) and lecture in self.courses_attached and lecture in self.courses_in_progress:
            if lecture in lecturer.scores:
                lecturer.scores[lecture] += [score]
            else:
                lecturer.scores[lecture] = [score]
        else:
            return 'Ошибка'

    def av_grade(self):
        grades_list = []
        for key, value in self.grades.items():
            for grade in value:
                grades_list.append(grade)
        av_grade = round(sum(grades_list) / len(grades_list), 2)
        return av_grade

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Student:\n{self.name}\n{self.surname}\nСредняя оценка за домашние задания: {self.av_grade()}\nКурсы в процессе обучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.av_grade() < other.av_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.scores = {}


class Lecturer(Mentor):

    def av_score(self):
        scores_list = []
        for key, value in self.scores.items():
            for score in value:
                scores_list.append(score)
        av_score = round(sum(scores_list) / len(scores_list), 2)
        return av_score

    def __str__(self):
        return f"Lecturer:\n{self.name}\n{self.surname}\nСредняя оценка за лекции: {self.av_score()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.av_score() < other.av_score()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Reviewer:\n{self.name}\n{self.surname}"


lecturer_1 = Lecturer('Some', 'Human')
lecturer_1.courses_attached += ['Python']

student_1 = Student('Ruoy', 'Eman', 'gender_1')
student_1.courses_in_progress += ['Python', 'Github']
student_1.courses_attached += ['Python', 'Github']
student_1.finished_courses += ['Введение в программирование']

student_1.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Python', 7)
student_1.rate_lect(lecturer_1, 'Python', 10)

reviewer_1 = Reviewer('Some', 'Guy')
reviewer_1.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)

lecturer_2 = Lecturer('Some2', 'Human2')
lecturer_2.courses_attached += ['Python']

student_2 = Student('John', 'Smith', 'gender_2')
student_2.courses_in_progress += ['Python', 'Github']
student_2.courses_attached += ['Python', 'Github']
student_2.finished_courses += ['Введение в программирование']

student_2.rate_lect(lecturer_2, 'Python', 5)
student_2.rate_lect(lecturer_2, 'Python', 5)
student_2.rate_lect(lecturer_2, 'Python', 5)

reviewer_2 = Reviewer('Some2', 'Guy2')
reviewer_2.courses_attached += ['Python']

reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)

print(f'Оценки студента №1 по курсу Python:', student_1.grades)
print(f'Оценки лектора №1 за лекции курсу Python:', lecturer_1.scores)
print()
print(f'Оценки студента №2 по курсу Python:', student_2.grades)
print(f'Оценки лектора №2 за лекции курсу Python:', lecturer_2.scores)
print()

print(reviewer_1)
print()
print(lecturer_1)
print()
print(student_1)
print()
print(reviewer_2)
print()
print(lecturer_2)
print()
print(student_2)
print()
print(f'Оценки студента №1 выше, чем оценки студента №2:', student_1 < student_2)
print(f'Оценки лектора №1 выше, чем оценки лектора №2:', lecturer_1 < lecturer_2)
print()

students_list = [student_1, student_2]
course = 'Python'


def course_av_grade(students_list, course):
    total = 0
    counter = 0
    for student in students_list:
        if course in student.courses_in_progress:
            student_course_av = round(sum(student.grades[course]) / len(student.grades[course]), 2)
            total += student_course_av
            counter += 1
            if counter == 0:
                return 'Нет студентов, изучающих данный курс.'
    return f'Средняя оценка студентов, изучающих курс Python:  {total / counter}'


lecturers_list = [lecturer_1, lecturer_2]
course = 'Python'


def course_av_score(lecturers_list, course):
    total = 0
    counter = 0
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            lecturer_course_av = round(sum(lecturer.scores[course]) / len(lecturer.scores[course]), 2)
            total += lecturer_course_av
            counter += 1
            if counter == 0:
                return 'Нет лекторов, читающих данный курс.'
    return f'Средняя оценка лекторов, читающих курс Python: {total / counter}'


print(f"Средняя оценка студентов по курсу {'Python'}: {course_av_grade(students_list, 'Python')}")
print(f"Средняя оценка лекторов по курсу {'Python'}: {course_av_score(lecturers_list, 'Python')}")

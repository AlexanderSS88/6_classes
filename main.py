class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.list = []


    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in lecturer.courses_attached) and (course in self.courses_in_progress):
            if course in lecturer.grade_book:
                lecturer.grade_book[course] += [grade]
            else:
                lecturer.grade_book[course] = [grade]
        else:
            return 'Ошибка'
        return lecturer.grade_book


    def __str__(self):
        middle = 0
        for course in self.courses_in_progress:
            if course in self.grades:
                for id in self.grades[course]:
                 middle += id
            else:
                print('Ошибка')
        middle_hw = middle / len(self.grades)
        text = (f'Имя: {self.name} \nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {middle_hw}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')
        return text


    def __lt__(self, other):
        middle = 0
        if not isinstance(other, Student):
            return
        else:
            for course in self.courses_in_progress:
                if course in self.grades:
                    for id in self.grades[course]:
                        middle += id
            middle_hw1 = middle / len(self.grades)
        middle2 = 0
        if not isinstance(other, Student):
            return
        else:
            for course in other.courses_in_progress:
                if course in other.grades:
                    for id in other.grades[course]:
                        middle2 += id
            middle_hw2 = middle2 / len(other.grades)
        return middle_hw1 < middle_hw2


    def middle(self, course):
        num = 0
        mid = 0
        self.list = [Vik, Oks, Mih]
        for student in self.list:
            if course in student.courses_in_progress:
                for id in student.grades[course]:
                    mid += id
                    num += 1
        mid = mid / num
        return mid


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_book = {}
        self.list = []


    def __str__(self):
        summ = 0
        numb = 0
        for position in self.grade_book:
            self.grade_book[position]
            for id in self.grade_book[position]:
                summ += id
                numb += 1
        summ = summ / numb
        text = (f'Имя: {self.name} \nФамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {summ}')
        return text

    def __lt__(self, other):
        middle = 0
        if not isinstance(other, Lecturer):
            return
        else:
            summ1 = 0
            numb1 = 0
            for position in self.grade_book:
                self.grade_book[position]
                for id in self.grade_book[position]:
                    summ1 += id
                    numb1 += 1
            summ1 = summ1 / numb1
            summ2 = 0
            numb2 = 0
            for position in other.grade_book:
                other.grade_book[position]
                for id in other.grade_book[position]:
                    summ2 += id
                    numb2 += 1
            summ2 = summ2 / numb2
        return summ1 < summ2


    def middle_lc(self, course):
        num = 0
        mid = 0
        self.list = [Roy, Tedd, Jack]
        for lecturer in self.list:
            if course in lecturer.grade_book:
                for id in lecturer.grade_book[course]:
                    mid += id
                    num += 1
        mid = mid / num
        mid = f'Средняя оценка за лекции всех лекторов в рамках курса {course} = {mid}'
        return mid


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (course in self.courses_attached) and (course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return student.grades

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text

Vik = Student('Viktor', 'Safronov', 'men')
Vik.finished_courses = ['python', 'c++']
Vik.courses_in_progress = ['ruby']
Oks = Student('Oksana', 'Vyazova', 'wom')
Oks.finished_courses = ['python', 'js']
Oks.courses_in_progress = ['c++']
Mih = Student('Michael', 'Dulin', 'men')
Mih.finished_courses = ['python', 'jawa']
Mih.courses_in_progress = ['js']
Roy = Lecturer('Roy', 'Jones')
Roy.courses_attached = ['python', 'jawa', 'ruby', 'c++', 'js']
Tedd = Lecturer('Tedd', 'Bihoff')
Tedd.courses_attached = ['python', 'jawa', 'ruby', 'c++', 'js']
Jack = Lecturer('Jack', 'Salevan')
Jack.courses_attached = ['python', 'jawa', 'ruby', 'c++', 'js']
Neo = Reviewer('Neo', 'Anderson')
Neo.courses_attached = ['python', 'jawa', 'ruby', 'c++', 'js']
Trinity = Reviewer('Trinity', 'Doolitle')
Trinity.courses_attached = ['python', 'jawa', 'ruby', 'c++', 'js']
Morfeus = Reviewer('Morfeus', 'Zeon')
Morfeus.courses_attached = ['python', 'jawa', 'ruby', 'c++', 'js']

print(f"Функция выставления оценки лектору {Roy.name}: {Vik.rate_lc(Roy, 'ruby', 7)}")
print(f"Функция выставления оценки лектору {Tedd.name}: {Oks.rate_lc(Jack, 'c++', 8)}")
print(f"Функция выставления оценки лектору {Jack.name}: {Mih.rate_lc(Tedd, 'js', 9)}", '\n')
print(f"Функция выставления оценки студенту {Vik.name} за дз: {Neo.rate_hw(Vik, 'ruby', 7)}")
print(f"Функция выставления оценки студенту {Oks.name} за дз: {Trinity.rate_hw(Oks, 'c++', 8)}")
print(f"Функция выставления оценки студенту {Mih.name} за дз: {Morfeus.rate_hw(Mih, 'js', 7)}", '\n')
print(Vik, '\n')
print(Oks, '\n')
print(Mih, '\n')
print(f'Средняя оценка за ДЗ всех студентов, проходящих курс ruby: {Vik.middle("ruby")}')
print(f'Средняя оценка за ДЗ всех студентов, проходящих курс c++: {Vik.middle("c++")}')
print(f'Средняя оценка за ДЗ всех студентов, проходящих курс js: {Vik.middle("js")}', '\n')
print(Roy, '\n')
print(Tedd, '\n')
print(Jack, '\n')
print(Vik < Oks)
print(Mih > Mih, '\n')
print(Roy < Tedd)
print(Jack > Roy, '\n')
print(Roy.middle_lc('ruby'))
print(Roy.middle_lc('js'), '\n')
print(Neo, '\n')
print(Trinity, '\n')
print(Morfeus)
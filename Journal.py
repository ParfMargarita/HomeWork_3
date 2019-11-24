import numpy
import Abiturient


class Journal:
    __students = []

    def __int__(self):
        pass

    def add_student(self, new_student):
        self.__students.append(new_student)
        print('The student was added to the journal!')
        print('-' * 100)

    # расчет среднего балла
    def grade_point_average(self):
        for stud in self.__students:
            marks = stud.get_marks()
            gpa = numpy.mean(marks)
            print(
                'The ' + stud.get_surname() + ' ' + stud.get_first_name() + ' ' + stud.get_patronymic() + 'grade point average =',
                gpa, '\n')
        print('-' * 100)

    # список абитуриентов, имеющих неудовлетворительные оценки
    def bad_marks(self):
        flag = False
        print('The list of bad students:')
        for stud in self.__students:
            marks = stud.get_marks()
            for mark in marks:
                if mark < 4:
                    print(
                        stud.get_id(),
                        ' ' + stud.get_surname() + ' ' + stud.get_first_name() + ' ' + stud.get_patronymic())
                    flag = True
        if not flag:
            print('\nThere are no students with bad marks!')
        print('-' * 100)

    # список абитуриентов, у которых сумма баллов выше заданной
    def above_specified_value(self, value):
        flag = False
        print('The list of students with summary mark above ' + str(value) + ':')
        for stud in self.__students:
            sum_mark = sum(stud.get_marks())
            if sum_mark > value:
                print(
                    stud.get_id(), ' ' + stud.get_surname() + ' ' + stud.get_first_name() + ' ' + stud.get_patronymic())
                flag = True
        if not flag:
            print('\nThere are no students with summary mark more then ', value, '!')
        print('-' * 100)

    # разрушение объекта
    def del_obj(self):
        del_flag = False

        if len(self.__students) == 0:
            print('There are no students in the journal!')
        else:
            value = 0

            while value not in (1, 2):
                value = int(
                    input('Define student by: \n\t1 - id\n\t2 - surname, first name\n'))

            if value == 1:
                id_value = int(input('Enter the id of student to delete:'))
                for stud in self.__students:
                    if id_value == stud.get_id():
                        self.__students.remove(stud)
                        print('The student was deleted!')
                        del_flag = True
                if not del_flag:
                    print('There is no a such student in the journal!')
            else:
                surname_value = input('Enter the surname of student to delete:')
                first_name_value = input('Enter the first name of student to delete:')
                for stud in self.__students:
                    if surname_value == stud.get_surname() and first_name_value == stud.get_first_name():
                        self.__students.remove(stud)
                        print('The student was deleted!')
                        del_flag = True
                if not del_flag:
                    print('There is no a such student in the journal!')
        print('-' * 100)

class Abiturient:
    __students_count = 0
    __id = 0
    __surname = None
    __first_name = None
    __patronymic = None
    __address = None
    __phone = 0
    __marks = []

    def __init__(self):

        self.__id = self.set_student_count()

        self.__surname = self.input_surname()
        self.__first_name = self.input_first_name()
        self.__patronymic = self.input_patronymic()
        self.__address = self.input_address()
        self.__phone = self.input_phone()
        self.__marks = self.input_marks()

        # Print student information
        print(
            'New student:\n\tID: {0} \n\tSurname: {1}\n\tFirst name: {2}\n\tPatronymic: {3}'.format(
                self.__id, self.__surname, self.__first_name, self.__patronymic))
        print('\tAddress: {0}\n\tPhone: {1}\n\tMarks: {2}\n'.format(self.__address, self.__phone, self.__marks))
        print('-' * 100)
    # Input student information

    def input_surname(self):
        try:
            surname = str(input('\nEnter surname:\t'))
            return surname
        except ValueError:
            print(' The surname must be the character string! Try again, please.\n')
            self.input_surname()

    def input_first_name(self):
        try:
            first_name = str(input('Enter first name:\t'))
            return first_name
        except ValueError:
            print(' The first name must be the character string! Try again, please.\n')
            self.input_first_name()

    def input_patronymic(self):
        try:
            patronymic = str(input('Enter patronymic:\t'))
            return patronymic
        except ValueError:
            print(' The patronymic must be the character string! Try again, please.\n')
            self.input_patronymic()

    def input_address(self):
        try:
            address = str(input('Enter the address:\t'))
            return address
        except ValueError:
            print(' The address must be the character string! Try again, please.\n')
            self.input_address()

    def input_phone(self):
        try:
            phone = int(input('Enter the phone:\t'))
            return phone
        except ValueError:
            print(' The phone must be numeral! Try again, please.\n')
            self.input_phone()

    def input_marks(self):
        add_marks = []
        add_flag = 'y'
        while add_flag in ('y', 'Y'):
            try:
                mark = int(input('Enter the mark:\t'))
                add_marks.append(mark)
                add_flag = input('\nTo add the mark press y or Y.\n')
            except ValueError:
                print(' The mark must be numeral! Try again, please.\n')
                # self.input_marks()
                add_flag = 'y'
        return add_marks

    # Get functions
    def get_id(self):
        return self.__id

    def get_surname(self):
        return self.__surname

    def get_first_name(self):
        return self.__first_name

    def get_patronymic(self):
        return self.__patronymic

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_marks(self):
        return self.__marks

    def set_student_count(self):
        Abiturient.__students_count += 1
        return Abiturient.__students_count

'''    def __init__(self, surname, first_name, patronymic, address, phone, marks):
        self.__students_count += 1

        self.__id = self.__students_count
        self.__surname = surname
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__address = address
        self.__phone = phone
        self.__marks = marks
        # Print student information
        print(
            '\nNew student:\n\tID: {0} \n\tSurname: {1}\n\tFirst name: {2}\n\tPatronymic: {3}'.format(
                self.__id, self.__surname, self.__first_name, self.__patronymic))
        print('\tAddress: {0}\n\tPhone: {1}\n\tMarks: {2}'.format(self.__address, self.__phone, self.__marks))
'''




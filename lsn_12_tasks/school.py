class Lesson:
    """
    |Parameters: positional   |
    |hours_per_lesson : int   |
    |student_score    : int   |
    """

    def __init__(self, hours_per_lesson: int):
        try:
            self.hours_per_lesson = int(hours_per_lesson)
        except ValueError:
            print('wrong format dude')


class English(Lesson):
    """
    Lesson as others
    Parameters : positional
    hours_per_lesson : int
    """

    def __init__(self, hours_per_lesson: int):
        super(English, self).__init__(hours_per_lesson)
        self.name = 'english'


class Ukrainian(Lesson):
    """
    Lesson as others
    Parameters : positional
    hours_per_lesson : int
    """

    def __init__(self, hours_per_lesson: int):
        super(Ukrainian, self).__init__(hours_per_lesson)
        self.name = 'ukrainian'


class Russian(Lesson):
    """
    Lesson as others
    Parameters : positional
    hours_per_lesson : int
    """

    def __init__(self, hours_per_lesson: int):
        super(Russian, self).__init__(hours_per_lesson)
        self.name = 'russian'


class Math(Lesson):
    """
    Lesson as others
    Parameters : positional
    hours_per_lesson : int
    """

    def __init__(self, hours_per_lesson: int):
        super(Math, self).__init__(hours_per_lesson)
        self.name = 'math'


class Physics(Lesson):
    """
    Lesson as others
    Parameters : positional
    hours_per_lesson : int
    """

    def __init__(self, hours_per_lesson: int):
        super(Physics, self).__init__(hours_per_lesson)
        self.name = 'physics'


class Person:
    """
    |Parameters : positional
    |age : int
    |name : str
    """
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Student(Person):
    STUDENT_COUNTER = 0

    def __init__(self, age: int, name: str):
        Student.STUDENT_COUNTER += 1
        super().__init__(age, name)
        self.h_per_w = 0
        self.lessons = []
        self.avg = 0

    def upd_score(self, lesson: (English, Ukrainian, Russian, Math, Physics), score):
        """Updating/making score for exact lesson for exact student"""
        try:
            for les in self.lessons:
                if les['name'] == lesson.name:
                    les.update({'name': lesson.name,
                                'score': score,
                                'lperweek': les['lperweek']})
                    self.avg = (self.avg + les['score']) / len(self.lessons)
                    return
        except (IndexError, AttributeError):
            print('Not found)')

    def add_lesson(self, lesson: (English, Ukrainian, Russian, Math, Physics)):
        """Adding lesson to student`s lessons"""
        try:
            for les in self.lessons:
                if les['name'] == lesson.name:
                    les.update({'name': lesson.name,
                                'score': les['score'],
                                'lperweek': les['lperweek'] + 1})
                    return
            self.lessons.append({'name': lesson.name,
                                 'score': 0,
                                 'lperweek': 1})
        except AttributeError:
            print('Not found)')

    def remove_lesson(self, lesson: (English, Ukrainian, Russian, Math, Physics)):
        """Removing lesson from student`s lessons"""
        try:
            for les in self.lessons:
                if les['name'] == lesson.name:
                    self.lessons.remove(les)
        except AttributeError:
            print('Not found)')


class Teacher(Person):
    """
    |Start salary = 1000                                                                 |
    |Start lvl = 0                                                                       |
    ------------------------------------------------------------------------------------ |
    |Salary koffs for professions:                                                       |
    |English - 1                                                                         |
    |Russian - 0.5                                                                       |
    |Ukrainian - 0.25                                                                    |
    |Math - 1.25                                                                         |
    |Physics - 1.25                                                                      |
    ------------------------------------------------------------------------------------ |
    |Parameters: positional                                                              |
    |age : int                                                                           |
    |name : str                                                                          |
    |proffesion : str                                                                    |
    ------------------------------------------------------------------------------------ |
    Methods:                                                                             |
    |set_salary(amount to increase:int) KOFFS not affecting salary adding on this method |
    |set_lvl(lvl_to_set:int) KOFFS affect salary adding by this method                   |
    |lvl_up() Up Teacher lvl by 1, KOFFS affecting salary adding by this method          |
    """

    START_SALARY = 1000
    KOFFS = {
        'english': 1,
        'russian': 0.5,
        'ukrainian': 0.25,
        'math': 1.25,
        'physics': 1.25
    }

    def __init__(self, age: int, name: str, proff: str):
        super(Teacher, self).__init__(age, name)
        self.salary = self.START_SALARY * self.KOFFS[proff]
        self.lvl = 0
        self.lvl_cost = 1000 * self.KOFFS[proff]
        self.profession = proff
        self.students = []

    def add_student(self, student: Student):
        """Adding a student to teacher class, updating salary"""

        if isinstance(student, Student):
            for les in student.lessons:
                if les['name'] == self.profession:
                    self.students.append({'name': student.name,
                                          'age': student.age,
                                          'avg': student.avg})
                    self._upd_salary()

    def set_salary(self, amount):
        """Set entered salary"""
        try:
            self.salary = int(amount)
        except ValueError:
            print('Input an integer')

    def _upd_salary(self):
        """Private method, helping to calc salary"""
        self.salary = (self.salary + self.lvl * self.lvl_cost * len(self.students))

    def lvl_up(self):
        """Lvl up teacher by 1"""

        self.lvl += 1
        self._upd_salary()

    def set_lvl(self, lvl):
        """Set entered lvl of teacher"""
        try:
            self.lvl += int(lvl)
            self._upd_salary()
        except ValueError:
            print('Input an integer')

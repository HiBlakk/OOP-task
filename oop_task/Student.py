class Student:
    def validate(self, name, group, average_mark):
        return isinstance(name, str) and isinstance(group, (int, str)) and isinstance(average_mark, (int, float)) and 0 <= average_mark <= 5

    def __init__(self, name, group, average_mark=0):
        if not self.validate(name, group, average_mark):
            print(self.validate(name, group, average_mark), '!')
            raise ValueError

        self.name = name
        self.group = group
        self.average_mark = average_mark
        self.degree = self._get_degree()

    def _get_degree(self):
        return NotImplemented

    def _get_grant(self, minimum, usual, maximum):
        if self.average_mark == 5:
            return maximum
        elif 4 <= self.average_mark < 5:
            return usual
        elif 3 < self.average_mark < 4:
            return minimum
        else:
            return 0

    def update_average_mark(self, average_mark):
        self.average_mark = average_mark

    def get_grant(self):
        return NotImplemented

    def __str__(self):
        return f"""(
    name: {self.name};
    group: {self.group};
    grant: {self.get_grant()}
    degree: {self.DEGREE}
)"""

from .Student import Student


class Aspirant(Student):
    DEGREE = 'Aspirant'

    def get_grant(self):
        return self._get_grant(3500, 4500, 5000)

    def _get_degree(self):
        return 'Aspirant'

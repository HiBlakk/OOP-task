from .Student import Student


class Bachelor(Student):
    DEGREE = "Bachelor"

    def get_grant(self):
        return self._get_grant(1500, 2000, 3000)

    def _get_degree(self):
        return 'Bachelor'

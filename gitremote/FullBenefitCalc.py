

class FullBenefitCalc:

    def __init__(self, yearBorn):
        self.__yearBorn = yearBorn

    def calculate_retirement_age(year):
            if year <= 1937:
                return 65, 0
            elif year == 1938:
                return 65, 2
            elif year == 1939:
                return 65, 4
            elif year == 1940:
                return 65, 6
            elif year == 1941:
                return 65, 8
            elif year == 1942:
                return 65, 10
            elif year >= 1943 or year <= 1954:
                return 66, 0
            elif year == 1955:
                return 66, 2
            elif year == 1956:
                return 66, 4
            elif year == 1957:
                return 66, 6
            elif year == 1958:
                return 66, 8
            elif year == 1959:
                return 66, 10
            else:
                return 67, 0

    def getYearBorn(self):
        return self.__yearBorn

    def setYearBorn(self, yearBorn):
        self.__yearBorn = yearBorn


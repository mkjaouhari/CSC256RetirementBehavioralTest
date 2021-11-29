

class FullBenefitCalc:

    def __init__(self, yearBorn):
        self.__yearBorn = yearBorn


    def obtainFullBenefits(self):
        age, months = self.getFullRetirementAge()
        yearOfRetirement = self.__yearBorn + age
        monthOfRetirement = self.__monthBorn + months
        if monthOfRetirement > 12:
            monthOfRetirement = monthOfRetirement % 12
            yearOfRetirement += 1

        return yearOfRetirement, self.getMonths().get(monthOfRetirement)


    def getFullRetirementAge(self):
        if self.__yearBorn <= 1937:
            return 65, 0
        elif self.__yearBorn == 1938:
            return 65, 2
        elif self.__yearBorn == 1939:
            return 65, 4
        elif self.__yearBorn == 1940:
            return 65, 6
        elif self.__yearBorn == 1941:
            return 65, 8
        elif self.__yearBorn == 1942:
            return 65, 10
        elif self.__yearBorn >= 1943 and self.__yearBorn <= 1954:
            return 66, 0
        elif self.__yearBorn == 1955:
            return 66, 2
        elif self.__yearBorn == 1956:
            return 66, 4
        elif self.__yearBorn == 1957:
            return 66, 6
        elif self.__yearBorn == 1958:
            return 66, 8
        elif self.__yearBorn == 1959:
            return 66, 10
        else:
            return 67, 0

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

    def getMonthBorn(self):
        return self.__monthBorn

    def getMonths(self):
        return self.__MONTHS

    def setYearBorn(self, yearBorn):
        self.__yearBorn = yearBorn

    def setMonthBorn(self, monthBorn):
        self.__monthBorn


def calculate_retirement_age(param):
    return None

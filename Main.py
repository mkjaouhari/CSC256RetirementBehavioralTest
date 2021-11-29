from gitremote.FullBenefitCalc import FullBenefitCalc


class Main():

    CURRENT_YEAR = 2021

    while(True):
        try:
            yearBorn = int(input("What year were you born in? "))
            if (yearBorn < 1900 or yearBorn > CURRENT_YEAR):
                print("Must enter year in or after 1900 and in or before current year")
                continue
        except:
            print("Must enter value of type int")
            continue
        break

    while(True):
        try:
            monthBorn = int(input("What month were you born in? "))
            if (monthBorn < 1 or monthBorn > 12):
                print("Must enter month value from 1 to 12 based on the respective month you were born in")
                continue
        except:
            print("Must enter value of type int")
            continue
        break

    fullBenefitCalc = FullBenefitCalc(yearBorn, monthBorn)

    retirementYear, retirementMonth = fullBenefitCalc.getFullRetirementAge()
    print("Your full retirement age is " + str(retirementYear) + " and " + str(retirementMonth) + " months")

    yourRetirementYear, yourRetirementMonth = fullBenefitCalc.obtainFullBenefits()
    print("This will be in " + str(yourRetirementMonth) + " of " + str(yourRetirementYear))

Main()



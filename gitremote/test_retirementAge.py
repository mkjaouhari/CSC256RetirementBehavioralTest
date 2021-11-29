from pytest_bdd import scenarios, given, when, then

import pytest
# def test_RetirementYears():
from gitremote.FullBenefitCalc import FullBenefitCalc


@scenarios("Calculate retirmement age for birth year of 1937")
def test_getRetirementAgeForYear1937():
    given("Application asks user for year they were born in")
    when("The user enters 1937 and presses enter")
    @then("Application returns that user can retire when they are 65 years old")
    def result():
        calc = FullBenefitCalc(1937)
        age, month = calc.calculate_retirement_age(1937)
        assert age == 65 and month == 0

@scenarios("Calculate retirmement age for birth year of 1938")
def test_getRetirementAgeForYear1938():
    given("Application asks user for year they were born in")
    when("The user enters 1938 and presses enter")
    @then("Application returns that user can retire when they are 65 years and 2 months old")
    def result():
        calc = FullBenefitCalc(1938)
        age, month = calc.calculate_retirement_age(1938)
        assert age == 65 and month == 2

@scenarios("Calculate retirmement age for birth year of 1939")
def test_getRetirementAgeForYear1939():
    given("Application asks user for year they were born in")
    when("The user enters 1939 and presses enter")
    @then("Application returns that user can retire when they are 65 years and 4 months old")
    def result():
        calc = FullBenefitCalc(1939)
        age, month = calc.calculate_retirement_age(1939)
        assert age == 65 and month == 4

@scenarios("Calculate retirmement age for birth year of 1940")
def test_getRetirementAgeForYear1940():
    given("Application asks user for year they were born in")
    when("The user enters 1940 and presses enter")
    @then("Application returns that user can retire when they are 65 years and 6 months old")
    def result():
        calc = FullBenefitCalc(1940)
        age, month = calc.calculate_retirement_age(1940)
        assert age == 65 and month == 6

@scenarios("Calculate retirmement age for birth year of 1941")
def test_getRetirementAgeForYear1941():
    given("Application asks user for year they were born in")
    when("The user enters 1941 and presses enter")
    @then("Application returns that user can retire when they are 65 years and 8 months old")
    def result():
        calc = FullBenefitCalc(1941)
        age, month = calc.calculate_retirement_age(1941)
        assert age == 65 and month == 8

@scenarios("Calculate retirmement age for birth year of 1942")
def test_getRetirementAgeForYear1942():
    given("Application asks user for year they were born in")
    when("The user enters 1942 and presses enter")
    @then("Application returns that user can retire when they are 65 years and 10 months old")
    def result():
        calc = FullBenefitCalc(1942)
        age, month = calc.calculate_retirement_age(1942)
        assert age == 65 and month == 10

@scenarios("Calculate retirmement age for birth year of 1943")
def test_getRetirementAgeForYear1943():
    given("Application asks user for year they were born in")
    when("The user enters 1943 and presses enter")
    @then("Application returns that user can retire when they are 66 years old")
    def result():
        calc = FullBenefitCalc(1943)
        age, month = calc.calculate_retirement_age(1943)
        assert age == 66 and month == 0

@scenarios("Calculate retirmement age for birth year of 1954")
def test_getRetirementAgeForYear1954():
    given("Application asks user for year they were born in")
    when("The user enters 1954 and presses enter")
    @then("Application returns that user can retire when they are 66 years old")
    def result():
        calc = FullBenefitCalc(1954)
        age, month = calc.calculate_retirement_age(1954)
        assert age == 66 and month == 0

@scenarios("Calculate retirmement age for birth year of 1955")
def test_getRetirementAgeForYear1955():
    given("Application asks user for year they were born in")
    when("The user enters 1955 and presses enter")
    @then("Application returns that user can retire when they are 66 years and 2 months old")
    def result():
        calc = FullBenefitCalc(1955)
        age, month = calc.calculate_retirement_age(1955)
        assert age == 66 and month == 2

@scenarios("Calculate retirmement age for birth year of 1956")
def test_getRetirementAgeForYear1956():
    given("Application asks user for year they were born in")
    when("The user enters 1956 and presses enter")
    @then("Application returns that user can retire when they are 66 years and 4 months old")
    def result():
        calc = FullBenefitCalc(1956)
        age, month = calc.calculate_retirement_age(1956)
        assert age == 66 and month == 4

@scenarios("Calculate retirmement age for birth year of 1957")
def test_getRetirementAgeForYear1957():
    given("Application asks user for year they were born in")
    when("The user enters 1957 and presses enter")
    @then("Application returns that user can retire when they are 66 years and 6 months old")
    def result():
        calc = FullBenefitCalc(1957)
        age, month = calc.calculate_retirement_age(1957)
        assert age == 66 and month == 6

@scenarios("Calculate retirmement age for birth year of 1958")
def test_getRetirementAgeForYear1958():
    given("Application asks user for year they were born in")
    when("The user enters 1958 and presses enter")
    @then("Application returns that user can retire when they are 66 years and 8 months old")
    def result():
        calc = FullBenefitCalc(1958)
        age, month = calc.calculate_retirement_age(1958)
        assert age == 66 and month == 8

@scenarios("Calculate retirmement age for birth year of 1959")
def test_getRetirementAgeForYear1959():
    given("Application asks user for year they were born in")
    when("The user enters 1959 and presses enter")
    @then("Application returns that user can retire when they are 66 years and 10 months old")
    def result():
        calc = FullBenefitCalc(1959)
        age, month = calc.calculate_retirement_age(1959)
        assert age == 66 and month == 10

@scenarios("Calculate retirmement age for birth year of 1960")
def test_getRetirementAgeForYear1960():
    given("Application asks user for year they were born in")
    when("The user enters 1960 and presses enter")
    @then("Application returns that user can retire when they are 67 years old")
    def result():
        calc = FullBenefitCalc(1960)
        age, month = calc.calculate_retirement_age(1960)
        assert age == 67 and month == 0

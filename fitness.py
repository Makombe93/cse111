# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime



def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender (Male or Female): ")
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your height (US Pounds): "))
    inches = float(input("Enter your weight (US Inches): "))

    # Call the compute_age function and compute age into years
    years = compute_age(birth_str)

    #Call the kg_from_lb function and convert weight to kgs
    kgs = kg_from_lb(pounds)

    #Call the cm_from_in function and convert height to cm
    cm = cm_from_in(inches)

    #Call body mass index function 
    bmi = body_mass_index(kgs, cm)

    #Call basal metabolic rate function
    bmr = basal_metabolic_rate(gender, kgs, cm, years)

    # Print the results for the user to see.
    print(f"Your age (years) is: {years}")
    print(f"Your weight is: {kgs : .1f}")
    print(f"Your height is: {cm : .1f}")
    print(f"Your Body mass index is: {bmi : .1f}")
    print(f"Your basal metabolic rate is: {bmr : .1f}")

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kgs = pounds *  0.45359237
    return kgs


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "Female":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    
    return bmr


# Call the main function so that
# this program will start executing.
main()

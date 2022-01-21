from datetime import date

# Getting the current date, as well as the user's birthdate
current_date = date.today()
birthdate = input("What is your birthdate? Enter MM/DD/YYYY\n")

# Formatting the birthdate and current_date variables
current_date = date(current_date.year, current_date.month, current_date.day)
birthdate = date(int(birthdate[6:10]), int(birthdate[0:2]),
                 int(birthdate[3:5]))

# Finding the user's age in days and subtracting it from 90yrs (32850 days)
age_days = current_date - birthdate
lifespan = 32850 - age_days.days

# Creating individual values for years, months, and days remaining
years_remaining = int((lifespan - (lifespan % 365))/365)
lifespan = lifespan % 365
months_remaining = int((lifespan-(lifespan % 31))/31)
days_remaining = lifespan % 31

print(f"You have {years_remaining} years, {months_remaining} months,"
      f"and {days_remaining} days left to live")

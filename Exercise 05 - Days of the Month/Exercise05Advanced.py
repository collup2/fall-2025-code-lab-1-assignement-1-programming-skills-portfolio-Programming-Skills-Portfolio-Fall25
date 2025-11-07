days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

month = input("Enter the name of the month (e.g., January): ").title()
if month in days_in_month:
    if month == "February":
        leap = input("Is it a leap year? (yes/no): ").lower()  # user has to choose whether or not it's a leap year
        if leap == "yes":
            print("Number of days: 29")  # if user says yes
        else:
            print("Number of days:", days_in_month[month])
    else:
        print("Number of days:", days_in_month[month])
else:
    print("Invalid month name. Please enter a correct month.")  # if the user enters an invalid month name then this is shown 
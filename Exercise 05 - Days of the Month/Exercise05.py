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

month = input("Enter the name of the month (e.g., January): ").title()  # user enters the name of the month
if month in days_in_month:
    print("Number of days:", days_in_month[month])  # the number of days in the provided month are displayed
else:
    print("Invalid month name. Please enter a correct month.")  # if the user enters an invalid month name then this is shown 
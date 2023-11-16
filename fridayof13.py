from datetime import date, timedelta

def find_friday_13(year):
    fridays_13 = []


    for month in range(1, 13):

        current_date = date(year, month, 13)


        if current_date.weekday() == 4:  # Friday is 4
            fridays_13.append(current_date)

    return fridays_13

# # # Example Usage
year_to_check = 2026  # Change this to the desired year
fridays_13_in_year = find_friday_13(year_to_check)

# Print the result
print(f"Fridays on the 13th in {year_to_check}:")
for friday in fridays_13_in_year:
    print(friday)

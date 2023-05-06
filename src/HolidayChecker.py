from datetime import date
import holidays

uk_holidays = holidays.UnitedKingdom()
print('01-01-2023' in uk_holidays) #Returns true if the inputted day is a holiday.
print('24-04-2023' in uk_holidays) #Returns false if the inputted day is not a holiday.

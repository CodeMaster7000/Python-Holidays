from datetime import date
import holidays

uk_holidays = holidays.UnitedKingdom() #Enter the country's holidays you would like to see here.
for i in holidays.UnitedKingdom(years = 2023).items(): #Enter calendar year here.
    print(i)

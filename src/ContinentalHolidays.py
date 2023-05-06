#Python program to print the holidays of a continent. For the sake of simplicity, the continent of North America has been used.

from datetime import date
import holidays

north_america = holidays.CA() + holidays.US()
print(north_america.country)
print(north_america.get('07-07-2023'))
print(north_america.get('07-04-2023'))

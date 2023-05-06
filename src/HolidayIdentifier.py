from datetime import date
import holidays

uk_holidays = holidays.UnitedKingdom()
print(uk_holidays.get('01-01-2023'))
print(uk_holidays.get('25-12-2023'))

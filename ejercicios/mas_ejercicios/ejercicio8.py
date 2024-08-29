# Realizar un programa que pida un mes y un año (superior a 1900) y muestre el
# calendario del mes

import calendar
cl = calendar.TextCalendar()
year = int(input("Dime el año:"))
month = int(input("Dime el mes:"))
calendario_sep = cl.formatmonth(year, month)
print(calendario_sep)
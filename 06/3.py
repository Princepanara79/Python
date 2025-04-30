# Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates
a = (1,1,2025)
b = (9,1,2025)
days = (b[0] - a[0]) + (b[1] - a[1]) * 30 + (b[2] - a[2]) * 365
print(f"Number of days between {a} and {b} is {days} days")
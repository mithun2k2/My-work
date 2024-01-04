num_hours = int(input("How many hours do you work every day?"))
num_days = int(input("How many days did you work this month?"))
pay_per_day = float(input("How much is your pay per day?"))
salary = num_hours * num_days * pay_per_day
print("My salary for the month is GBP:{} before tax".format(salary))
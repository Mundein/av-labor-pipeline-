import pandas
import random
import datetime

markets = ["Los Angeles", "San Francisco", "Phoenix", "Denver", "Manhattan", "Portland", "San Diego", "Chicago", "San Antonio", "New Orleans"]
roles = ["Site Associate", "Driver", "Advanced Site Associate", "Advanced Driver", "Mapper", "Lead"]
start_date = datetime.date(2025, 10, 1)
end_date = datetime.date(2026, 6, 1)

total_days = (end_date - start_date).days
master_data = []

for i in range(total_days):
  for j in range(len(markets)):
    headcount = random.randint(15, 30)
    for k in range(headcount):
      random_num = random.randint(1,5)
      if random_num == 4:
        market = markets[j].lower()
      elif random_num == 3:
        market = markets[j].upper()
      else:
        market = markets[j]
      if random_num == 1:
        employee_id = None
      else:
        employee_id = random.randint(10000, 99999)
      role = random.choice(roles)
      hours_logged = random.randint(2, 10)
      employee_data = {"date": (start_date + datetime.timedelta(i)), "market": market, "employee_id": employee_id, "role": role, "hours": hours_logged}
      if random_num == 5:
        master_data.append(employee_data)
        master_data.append(employee_data)
      else:
        master_data.append(employee_data)

df = pandas.DataFrame(master_data)
df.to_csv('output.csv', index=False)

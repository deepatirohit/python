import datetime


date = datetime.date(2025, 4, 28)
today = datetime.date.today()
time = datetime.time(12,30, 0)
currentTime = datetime.datetime.now()


print(date)
print(today)
print(time)
print(currentTime)

target_dateTime = datetime.datetime(2029, 2, 2, 12, 24, 9)
current_dateTime = datetime.datetime.now()

if target_dateTime < current_dateTime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")
    

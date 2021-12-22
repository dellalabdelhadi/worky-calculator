from datetime import datetime

Start = datetime.strptime('24/7/2021 19:01',"%d/%m/%Y %H:%M")
Finsh = datetime.strptime('24/7/2021 04:04',"%d/%m/%Y %H:%M")

WorkingHours = Finsh - Start
print("Working hours " + str(WorkingHours))

startbreak = datetime.strptime('24/7/2021 20:52',"%d/%m/%Y %H:%M")
finishbreak = datetime.strptime('24/7/2021 21:31',"%d/%m/%Y %H:%M")

pausetimereslut = finishbreak - startbreak
print("Break duration " + str(pausetimereslut))

Total_working_hours = WorkingHours - pausetimereslut
print("Total of working hours " + str(Total_working_hours))

Working_hours_in_minutes = Total_working_hours.total_seconds()
finalinminutes = Working_hours_in_minutes // 60

#finalinminutes * the amount of money you are making per minute. Example: if you are making 20$ per hour, divide 20$ by 60min and you will get 0.33333
money = finalinminutes * 0.246833333 
print("You've made today " + str(money))

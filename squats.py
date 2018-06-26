day=0
squats=0
total=0
print("Enter the no. of squats you did on each day for the last one week and don't lie! \n")

while day<=6:
    day=day+1
    squats=int(input("Squats on day {}: ".format(day)))
    total=total+squats
    
avg=total/day
print("In the last {} days, you did an average of {} squats!".format(day,avg))
import time

timestamp = int(time.strftime('%H'))

print('time right now: ',time.strftime('%H:%M:%S'),end="\n")

if(5 <= timestamp <=11 ) :
    print("Good Morning!")
elif (12 <= timestamp <= 15 ) :
    print("Good Afternoon!")
elif (16 <= timestamp <= 18 ) :
    print("Good Evening!")
elif(19 <= timestamp <= 23) :
    print("Good Night")

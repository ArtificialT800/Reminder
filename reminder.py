import time

text = input("What shall I remind you about?: ")
local_time = float(input("In how many Minutes?: "))
local_time = local_time * 60
time.sleep(local_time)
print("It's time to " + text)


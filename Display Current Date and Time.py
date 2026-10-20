# 15. Display Current Date and Time

import datetime

current_time = datetime.datetime.now()

print("Current Date:", current_time.strftime("%d-%m-%Y"))
print("Current Time:", current_time.strftime("%I:%M:%S %p"))

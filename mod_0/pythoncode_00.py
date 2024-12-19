from datetime import datetime

right_this_minute = datetime.today().minute

if right_this_minute % 2 == 0:
    print("This minute")
else:
    print("Not minute.")

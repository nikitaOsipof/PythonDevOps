from datetime import datetime

right_this_minute = datetime.today().minute

print("str", str(datetime.today()))
print("repr", repr(datetime.today()))

'''

if right_this_minute % 2 == 0:
    print("This minute", str(datetime.today()))
else:
    print("Not minute.", repr(datetime.today()))

'''


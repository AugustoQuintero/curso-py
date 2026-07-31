from datetime import datetime
import pytz

tz = pytz.timezone('America/Bogota')
print(datetime.now(tz))




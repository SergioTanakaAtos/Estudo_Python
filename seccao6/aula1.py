from datetime import datetime
from pytz import timezone
#data_str = '2022-04-20 07:49:22'
#str_format = '%Y-%m-%d %H:%M:%S'

#data = datetime.strptime(data_str,str_format)
#data = datetime(2023,2,20,7,30,20)
data = datetime.now(timezone('Asia/Tokyo'))
print(data)


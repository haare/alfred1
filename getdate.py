

from datetime import datetime, timedelta
import sys


#좋네


_str_weekday = ['월', '화', '수', '목', '금', '토', '일']

week_str = sys.argv[1]

date_now = datetime.now()
date_result = datetime.now()
date_ref_monday = date_now - timedelta(days = date_now.weekday())

if week_str == "mon":
	date_result = date_ref_monday + timedelta(days=0)
elif week_str == "tue":
	date_result = date_ref_monday + timedelta(days=1)
elif week_str == "wed":
	date_result = date_ref_monday + timedelta(days=2)
elif week_str == "thu":
	date_result = date_ref_monday + timedelta(days=3)
elif week_str == "fri":
	date_result = date_ref_monday + timedelta(days=4)
elif week_str == "sat":
	date_result = date_ref_monday + timedelta(days=5)
elif week_str == "sun":
	date_result = date_ref_monday + timedelta(days=6)

print("(" + date_result.strftime("%m/%d") + "," + _str_weekday[date_result.weekday()] + ")")
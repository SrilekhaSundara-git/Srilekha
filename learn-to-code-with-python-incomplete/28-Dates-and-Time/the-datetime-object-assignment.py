from datetime import datetime
#Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:
today = datetime.today()
#The day of the week, abbreviated (i.e. "Fri" )
previous_date = today.replace(year = 2000, month = 11, day = 17, hour = 18, minute = 00, second =00)
#Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

#The day of the week, abbreviated (i.e. "Fri" )

#today = datetime(2000, 11, 17, 6, 0, 0)

print(previous_date.strftime("%a"))
#Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

#The full month name, the zero-padded day, the four-digit year. The day and year should be separated by a comma and a space (i.e. "November 17, 2000")

#today = datetime(2000, 11, 17, 6, 0, 0)

print(previous_date.strftime("%B %d, %Y"))
#Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

#The day of the year (i.e. "273")

#today = datetime(2000, 11, 17, 6, 0, 0)

print(previous_date.strftime("%j"))
#Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

#The week number of the year (i.e. "46")

#today = datetime(2000, 11, 17, 6, 0, 0)

print(previous_date.strftime("%U"))

#Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

#The time with a zero-padded hour, zero-padded minute, zero-padded second and AM / PM designation (i.e. "06:00:00 AM")

#today = datetime(2000, 11, 17, 6, 0, 0)

print(previous_date.strftime("%I:%M:%S %p"))
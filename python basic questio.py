# 1st answer
# print("Twinkle, twinkle,little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
# 2nd answer
'''
import sys
print("python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
'''
# print current date and time
'''
import datetime
now = datetime.datetime.now()
print("current datetime: ")
print(now.strftime("%y -%m -%d %H: %M: %S"))
'''
# display the first and last colors form a given list.
#color_list = ["Red", "green", "White", "Black"]
#print( "%s %s "%(color_list[0], color_list[3]))
# displaya asimple examination schedule
'''
exam_st_date=(11, 12, 2014)
print("The examination start form " "%i/%i/%i" %(exam_st_date))
'''
# the calendar for a given month

import calendar
y = int(input("Enter the year: "))
m = int(input("Enter the month:"))
print(calendar.month(y, m))

# to print the following document
'''
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------
""")
'''
# The number of days between two dates
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
middle_days = l_date - f_date
print(middle_days)
# to get the volume of a sphere with radius six
pie = 3.141592
r = 216
v = 4.0/3.0 * 216 * 3.1416
print(" Volume of a Sphere: ", v)

# using python class object
class student:
    roll = " "
    gpa = " "
rahim = student()
rahim.roll = 121
rahim.gpa = 8.91
print(f"roll: {rahim.roll} ,gpa {rahim.gpa}")
karim = student()
karim.roll = 122
karim.gpa = 8.47
print(f"roll: {karim.roll},gpa{karim.gpa}")

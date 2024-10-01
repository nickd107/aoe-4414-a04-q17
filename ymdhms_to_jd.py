# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second...
#   Converts normal time to Julian Date
# Parameters: Normal time
#   year:
#   month: 
#   day: 
#   hour: 
#   minute: 
#   second:

# Output: Julian Date
#   jd_frac:

#
# Written by Nick Dickson

# import Python modules
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

## calculate demoninator
# (eccentricity, latitude in radians)
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-ecc**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments
year = float('nan')  
month = float('nan') 
day = float('nan') 
hour = float('nan') 
minute = float('nan')  
second = float('nan') 

# parse script arguments
# if len(sys.argv) == 7:
#   year = int(sys.argv[1])
#   month = int(sys.argv[2])
#   day = int(sys.argv[3])
#   hour = int(sys.argv[4])
#   minute = int(sys.argv[5])
#   second = float(sys.argv[6])
# else:
#   print(\
#     'Usage: '\
#     'python3 ymdhms_to_jd.py year month day hour minute second'\
#   )
#   exit()
# if len(sys.argv) == 7:
#   year = float(sys.argv[1])
#   month = float(sys.argv[2])
#   day = float(sys.argv[3])
#   hour = float(sys.argv[4])
#   minute = float(sys.argv[5])
#   second = float(sys.argv[6])
# else:
#   print(\
#     'Usage: '\
#     'python3 ymdhms_to_jd.py year month day hour minute second'\
#   )
#   exit()
# ### script below this line ###

# JD = int(day-32075 + 1461*(year+4800+(month-14)/12)/4 + 367*(month-2-(month-14)/12*12)/12 - 3*((year+4900+(month-14)/12)/100)/4)
# JDmid = JD - 0.5
# Dfrac = (second + 60*(minute + 60*hour))/86400
# jd_frac = JDmid + Dfrac

# print(jd_frac)

if len(sys.argv) == 7:
     year = int(sys.argv[1])
     month = int(sys.argv[2])
     day = int(sys.argv[3])
     hour = int(sys.argv[4])
     minute = int(sys.argv[5])
     second = float(sys.argv[6])
else:
  print(\
    'Usage: '\
    'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()
### script below this line ###

JD = day - 32075 + 1461*(year+4800-(14-month)//12)//4 + 367*(month-2+(14-month)//12*12)//12 - 3*((year+4900-(14-month)//12)//100)//4
JDmid = JD - 0.5
Dfrac = (second + 60*(minute + 60*hour))/86400
jd_frac = JDmid + Dfrac

print(jd_frac)
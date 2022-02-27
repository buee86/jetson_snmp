#!/usr/bin/env python3

# Reads the content of the file where the load is stored
f=open("/sys/devices/virtual/thermal/thermal_zone2/temp","r")
contents=f.read()
contents=contents.strip()

# Conversion to a friendly format
contents=((float(contents) / 1000))

# Since this is called by the SNMPd daemon on demand, all we need to do is print the output for graphing)
# Note that SNMP reads everything as a string, but the float casting here is a small attempt at sanitizing the value
print(float(contents))

f.close()
exit(0)

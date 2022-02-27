#!/usr/bin/env python3

# Reads the content of the file where the load is stored
f=open("/sys/devices/gpu.0/load","r")
contents=f.read()
contents=contents.strip()

# Since this is called by the SNMPd daemon on demand, all we need to do is print the output for graphing)
# Note that SNMP reads everything as a string, but the int casting here is a small attempt at sanitizing the value
print(int(contents))

f.close()
exit(0)

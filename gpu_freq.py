#!/usr/bin/env python3
#/sys/devices/gpu.0# cat devfreq/57000000.gpu/cur_freq

# Reads the content of the file where the frequency is stored
f=open("/sys/devices/gpu.0/devfreq/57000000.gpu/cur_freq","r")
contents=f.read()
contents=contents.strip()

# Convert to GHz (if memory serves)
contents=(((int(contents) / 1000) / 1000))

# Since this is called by the SNMPd daemon on demand, all we need to do is print the output for graphing)
# Note that SNMP reads everything as a string, but the int casting here is a small attempt at sanitizing the value
print(int(contents))

# Cleanup
f.close()
exit(0)

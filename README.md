# SNMP Scripts for the NVIDIA Jetson Nano

### **Disclaimer**: My Jetson has been down for over a year due to a failing fan and I haven't had the time to replace the fan. All of this is dated and going off of my [admittedly horrid] memory. Some tweaking may be needed. This was a request from Reddit user /u/IMayHaveGoogledThat which *I think* stemmed from [this post](https://www.reddit.com/r/LibreNMS/comments/eog5xa/what_am_i_missing_with_custom_oids/)

---

## Instructions
Of course, any commands are to be executed on the Nano, either directly or via SSH
1. Update the Nano, of course `sudo apt clean && sudo apt update && sudo apt upgrade && sudo apt autoremove && sudo apt clean`
Yes, some of these are unnecessary, just my standard practice for keeping up to date and getting rid of clutter
2. Install snmpd on the Nano `sudo apt install snmpd`
3. Install *python3*, `sudo apt install python3` --- **The scripts will not work with python2, although they could with some mild modifications**
4. I would recommend becoming root at this point just because it's easier. The remainder of the commands are assuming that you're root. If you do not want to become root, tack the "sudo" on the front of each command
5. Might as well go directly to the snmp folder `cd /etc/snmp`
6. Make a backup of the default snmpd.conf file `mv snmpd.conf snmpd.conf.default`
7. Clone this repo `git clone https://github.com/buee86/jetson_snmp.git`, which should put a new folder in your current directory, *jetson_nano*
8. Copy the Python files to the directory `cp jetson_nano/*.py ./`
9. Copy the modified snmpd.conf file to the current directory `cp jetson_nano/*.conf ./`
10. Edit the snmpd.conf. Anything in square brackets needs to be filled out. `sysLocation` and `sysContact` are optional, but you **will** need to provide a community name, the default in the file is read-only.
11. Ensure proper permissions*
12. Restart snmpd to take on the new conf file `service snmpd restart`

\* - The permissions is a whole weird thing. I *believe* the user/group running SNMPd is "Debian-snmp". This can be checked with `ps aux | grep snmp`. This user needs the ability to execute the .py scripts. I believe I added my base user to the "Debian-snmp" group which allowed me to edit the files while still allowing the "Debian-snmp" user to execute the scripts. As for the snmpd.conf file, just match permissions with the original.

---

## Where to go from here?
Well, that's up to you. Using snmp_extend is great fun and it helps if you have an intermediate understanding of how SNMP functions and the structure of the trees.  Beyond this point, where to go is up to you.  If you run an snmpwalk against the Jetson now, you should be able to see the values returned. You can grep for the terms as seen in the snmpd.conf file. For example, `[snmpwalk command] | grep GPU_LOAD` will give you the SNMP line for the GPU_LOAD as pulled via the script.

You may need the numerical representation of the OID vs. the text version. Easy-peasy, you need to use `snmptranslate` ([doc here](https://net-snmp.sourceforge.io/tutorial/tutorial-5/commands/snmptranslate.html)). This will be a requirement, as I understand it, due to any snmp_extend scripts resulting in randomized OID values.

I did the best I could based on memory, hopefully this helps others.
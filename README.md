# Find-ports-that-haven-t-been-used-in-6-weeks

SSHs to a switch and looks at each port to see when the last input was, anything that hasn't ever gotten an input, or has been up for a year is reported as old, if it's uptime is mesured in weeks it compairs the number of weeks to a variable to see if it's reported as being unused.

Example output

Q:\Himes\Python in process\Junk work>Look for unused ports.py
Username: dhimes3-net
Password:
10.9.106.29  Unused Interfaces
FastEthernet1 never
TenGigabitEthernet1/1 never
TenGigabitEthernet1/2 never
GigabitEthernet1/4 never
GigabitEthernet2/2 never
GigabitEthernet2/4 51w0d
GigabitEthernet2/16 46w3d
GigabitEthernet2/18 never
GigabitEthernet2/22 never
GigabitEthernet2/29 never
GigabitEthernet2/33 never
GigabitEthernet2/35 never
GigabitEthernet2/41 51w0d
GigabitEthernet2/43 never
GigabitEthernet2/45 never
GigabitEthernet2/47 never
GigabitEthernet2/48 never
GigabitEthernet3/8 never
GigabitEthernet3/12 never

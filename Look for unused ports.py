from common_functions import *
from build_conn_base import *

#NOTE THIS DOES NOT TAKE UPTIME INTO CONCIDERATION: IF A PORT HAS NEVER GOTTEN INPUT
# AND UPTIME IS 2 WEEKS THE PORT WILL SHOW UP AS UNUSED

#lines that are automatically mean it's been unused for more than a few weeks (year or never currently)
old_lines = ['never','y']
#How many weeks do you want to look at
number_of_weeks_we_want = 6

for ip in ips:
    print (ip," Unused Interfaces")

    net_connect = make_connection(ip, username, password)
    if net_connect == None:
        continue
    #This command shows the interface line, and when the last input was
    command = "sho int | inc line prot|Last inp"
    output = run_command_on_net_connect(net_connect, command)
    #Break the input up into a list 1 line per string, CiscoConfparse needs it this way
    output = output.split("\n")
    #Break it up per interface, and only look at down interfaces
    interfaces = find_child_text(output, "line protocol is down")
    for interface in interfaces:
        #If we want this interface
        unused = False
        #Break the last input line down into just the info we want (like this: 6w0d)
        input_line = interface[1]
        input_line = input_line.lstrip(" ")
        last_input = input_line.split(',')[0]
        last_input = last_input.split(' ')[-1]

        #See if anything is in the time that automatically means it's unused
        for old_line in old_lines:
            if old_line in last_input:
                #print (old_line,last_input)
                unused = True
        #Dig into the output if w is there
        if 'w' in last_input:
            #If it's something like 1y41w the changing the output to int will fail with the Y there, but the for
            #Loop above will change it to true, in which case we don't care
            try:
                weeks = last_input.split("w")[0]
                #If the output is something like 6w0d just the 6 will be converted over then we compair that to the
                #Number of weeks we want it to be down for.
                if int(weeks)>=number_of_weeks_we_want:
                    unused = True
            except:
                pass
        if unused == True:
           phy_int = interface[0].split(" ")[0]
           print (phy_int,last_input)






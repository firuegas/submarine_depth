#!/usr/bin/env python

import re
import sys

# Set the input file name
# (The program must be run from within the directory 
# that contains this data file)
InFileName = '/ufrc/zoo6927/share/pcfb/examples/ctd.txt'

# Open the input file for reading
try:
	InFile = open(InFileName, 'r')
except:
	print "Cannot open the file you want: %s" %(InFileName)
	sys.exit(1)
	


# Initialize the counter used to keep track of line numbers
LineNumber = 0

#Time to reach 800 meter
# Loop through each line in the file
for Line in InFile:
	Line=Line.strip('\n')

	if LineNumber > 0:
		# Print the line
		ElementList=Line.split(',')
		timedive = re.search('^\d+\/\d+\/\d+\s+(\d+\:\d+\:\d+)', ElementList[1]).group(1) 
		depth = float(ElementList[4]) 
		if LineNumber  == 1:
			inittime = timedive
		if  depth >= 800:
			endtime = timedive
			print "Problem a: Time changed from %s to %s to reach the depth %s" %(inittime, endtime, depth)
			# Getting the differenct of time
			# Convert string time to second and take the difference
			time_start = map(int, re.split(r"[:,]", inittime))
			time_startSec = time_start[0]*3600 + time_start[1]*60 + time_start[2] 
			time_end = map(int, re.split(r"[:,]", endtime))
			time_endSec = time_end[0]*3600 + time_end[1]*60 + time_end[2]
			timeReq = (time_endSec - time_startSec)/60.0
			print "So the required time was %s minutes to reach the depth of 800 m" %(timeReq)
			break
	LineNumber = LineNumber + 1
line = LineNumber

# Time stayed below 800 meter
LineNumber = 0
for Line in InFile:
        Line=Line.strip('\n')
        if LineNumber >=line:
                # Print the line
                ElementList=Line.split(',')
                timedive = re.search('^\d+\/\d+\/\d+\s+(\d+\:\d+\:\d+)', ElementList[1]).group(1)
                depth = float(ElementList[4])
		if depth <800:
                        stay800 = timedive
                	# Getting the differenct of time
                        # Convert string time to second and take the difference
                        time_800 = map(int, re.split(r"[:,]", stay800))
			time_800S = time_800[0]*3600 + time_800[1]*60 + time_800[2]
			time_stay = (time_800S - time_endSec)/60.0
			print "Problem b: The submarine was below the 800 level for %s minutes" %(time_stay)
			break
	LineNumber = LineNumber +1
print(LineNumber)


#Getting maximum depth
LineNumber = 0
maxdepth = 0
for Line in InFile:
        Line=Line.strip('\n')
        if LineNumber >0:
                # Print the line
                ElementList=Line.split(',')
                depth = float(ElementList[4])
                if depth >= maxdepth:
                        maxdepth = depth
        LineNumber = LineNumber +1
print "Problem c: The maximum depth the submarine travelled was %s" %( maxdepth)
OutFileName= 'maxdepth.out'
OutFile=open(OutFileName, 'a')
OutFile.write(str(maxdepth))
InFile.close()

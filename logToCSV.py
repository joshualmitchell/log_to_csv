import re

with open("eventlog.txt") as file:
	lines = file.read()
	eventsList = re.findall("(Event\[)[0-9]+(\])", lines)
	numEvents = len(eventsList)
	print(numEvents)
	log = []
	# while True:
    # line = file.readline().strip()
    # if line == '':
        # either end of file or just a blank line.....
        # we'll assume EOF, because we don't have a choice with the while loop!
        # break

	# for line in file:
		#stripped_line = line.rstrip()
		# log.append(stripped_line)
	#for line in log:
		# print(line)
		# print(line)
		# print("---------------------------")
# Process: importing libraries
import time

# Process: Timer starts
starttime = time.time()
lasttime = starttime
lapnum = 1

print("Press ENTER to occurrence_count laps.\nPress CTRL+C to stop")

try:
	while True:

		# Process: Input for the ENTER key press
		input()

		# Process: The current lap-time
		laptime = round((time.time() - lasttime), 2)

		# Process: Total time elapsed
		# Process: since the timer started
		totaltime = round((time.time() - starttime), 2)

		# Process: Printing the lap number,
		# Process: lap-time and total time
		print("Lap No. "+str(lapnum))
		print("Total Time: "+str(totaltime))
		print("Lap Time: "+str(laptime))

		print("*"*20)

		# Process: Updating the previous total time
		# Process: and lap number
		lasttime = time.time()
		lapnum += 1

# Process: Stopping when CTRL+C is pressed
except KeyboardInterrupt:
	print("Done")
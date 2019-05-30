import os
import sys

dird = ""
count = "1"
rands = False

if __name__ == "__main__":
	argsLength = len(sys.argv)
	for p in range(0, argsLength):
		arg = sys.argv[p]
		if(arg == "--dir" or arg == "-d"):
			if p + 1 <= argsLength:
				dird = sys.argv[p + 1]
				if dird is None:
					print(arg + " called but information was not found!")
					exit()
			else:
				print(arg + " called but information was not found!")
				exit()
		if(arg == "--count" or arg == "-c"):
			if p + 1 < argsLength:
				count = sys.argv[p + 1]
				if count is None:
					print(arg + " called but information was not found!")
					exit()
			else:
				print(arg + " called but information was not found!")
				exit()
		if(arg == "--rand" or arg == "-r" or arg == "--random"):
			if p + 1 < argsLength:
				t = sys.argv[p + 1]
				if t is None:
					print(arg + " called but information was not found!")
					exit()
				if t.lower() == "true":
					rands = True
				if t.lower() == "false":
					rands = False
			else:
				print(arg + " called but information was not found!")
				exit()
		
	if (dird == ""):
		print("Directroy not set! Please set with --dir or -d!")
		exit()
	
	print("Directory: " + dird)
	print("Count: " + count)
	print("Use Randoms: " + str(rands))
		

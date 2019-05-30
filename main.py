from google_images_download import google_images_download   #importing the library
import os
import sys

response = google_images_download.googleimagesdownload()
foundFolders = []

def looplas(limit, terms):
	for p in foundFolders:
		downloadlots(p, limit, terms)
		foundFolders.remove(p)

def downloadlots(dirct, limit, terms):
	arguments = {"keywords":terms,"limit":limit,"print_urls":True,"output_directory":dirct, "no_directory":True}
	paths = response.download(arguments)
	print(paths)

def ma(dird, limit, terms):
	foundFolders.append(dird)
	output = [dI for dI in os.listdir(dird) if os.path.isdir(os.path.join(dird,dI))]
	for f in output:
		ot = [dF for dF in os.listdir(os.path.join(dird,f)) if os.path.isdir(os.path.join(dird, f, dF))]
		foundFolders.append(os.path.join(dird, f))
		for f2 in ot:
			oy = [dD for dD in os.listdir(os.path.join(dird,f,f2)) if os.path.isdir(os.path.join(dird, f, f2, dD))]
			foundFolders.append(os.path.join(dird, f, f2))
			for s in oy:
				foundFolders.append(os.path.join(dird, f, f2, s))
	
	looplas(limit, terms)

def writelog(dird):
	logfile = os.path.join(dird, "logs.txt")
	f = open(logfile, "w+")
	for ob in foundFolders:
		f.write(ob + "\n")

def frun(dird, limit, terms, loadLog):
	try:
		if loadLog:
			logfile = os.path.join(dird, "logs.txt")
			if os.path.exists(logfile):
				print "\nAttempting to reload log file\n"
				f = open(logfile, "r")
				if f.mode == "r":
					le = f.readlines()
					for x in le:
						foundFolders.append(x.rstrip())
				print foundFolders
				looplas(limit, terms)
					
				if len(foundFolders) >= 1:
					looplas(limit, terms)
			else:
				print "\nHey! Log file does not exist! \nRunning without loading log!\n"
				frun(dird, limit, terms, False)
		else:
			ma(dird, limit, terms)
		writelog(dird)
	except KeyboardInterrupt:
		print "\nInterrupted... Writing leftovers to log file."
		writelog(dird)
		exit()

def printHelp():
	print("Format is python-imager (DIR) (# OF IMAGES)")

dird = ""
count = "1"
rands = False
terms = ""

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

	try:
		data=[]
		namesPath=os.path.join(dird, "names.txt")
		if os.path.exists(namesPath):
			with open(namesPath, 'r') as f:
				data = f.readlines()
			
			print(data)
			print("\n")
			
			for s in data:
				terms = terms + s.replace("\n", '') + ", "
			
			print(terms)
			print("\n")
			
			frun(dird, count, terms, True)
		else:
			print("names.txt not found. Assuming commandline usage.")
			frun(dird, count, terms, True)
		
	except Exception as e:
		print(e)
		exit()
	#if sys.argv[1] == "--log":
	#	frun(sys.argv[2], sys.argv[4], sys.argv[3], True)
	#else:
	#	frun(sys.argv[1], sys.argv[3], sys.argv[2], False)
